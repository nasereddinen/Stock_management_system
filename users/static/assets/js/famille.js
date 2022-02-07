$(document).ready(function() {
  $('.table').DataTable();
} );

$(function () {
  const swalWithBootstrapButtons = Swal.mixin({
    customClass: {
        confirmButton: 'btn btn-primary',
        cancelButton: 'btn btn-gray'
    },
    buttonsStyling: false
});
    var loadForm = function () {
      var btn = $(this);
      $.ajax({
        url: btn.attr('data-url'),
        type: 'get',
        dataType: 'json',
        beforeSend: function () {
          $("#modal-famille").modal("show");
        },
        success: function (data) {
          $("#modal-famille .modal-content").html(data.html_form);
        }
      });
    };
   
    var saveForm = function () {
      var form = $(this);
      $.ajax({
        url: form.attr("action"),
        data: form.serialize(),
        type: form.attr("method"),
        dataType: 'json',
        success: function (data) {
          if (data.form_is_valid) {
            $("#famille-table tbody").html(data.html_famille_list);
            $("#modal-famille").modal("hide");
            swalWithBootstrapButtons.fire({
              icon: 'success',
              title: 'success',
              text: 'Nouvelle famille ajouter',
              showConfirmButton: true,
              timer: 1500
          })

          }
          else {
            $("#modal-famille .modal-content").html(data.html_form);
          }
        }
      });
      return false;
    };

    var valid = (function () {
      $.ajaxSetup({
        headers: {
            "X-CSRFToken": document.querySelector('[name=csrfmiddlewaretoken]').value,
        }
    });
  
      var id_famille = $(this).val();
      console.log(id_famille)
      $.ajax({
      url: "valid_famille",
      method: 'POST',
      data: {
        'id_famille': id_famille
      },
      dataType: 'json',
      success: function (data) {
        if (data.taken) {
          swalWithBootstrapButtons.fire({
            icon: 'warning',
            title: 'exist alert',
            text: 'this name already exist',
            showConfirmButton: true,
            timer: 1500
        })
        }
      }
    });
  });

    $(".js-load-famille").click(loadForm);
    $("#modal-famille").on("submit", ".js_create_famille_form", saveForm);

    $("#famille-table").on("click", ".js-update-famille", loadForm);
    $("#modal-famille").on("submit", ".js_update_famille_form", saveForm);

    $("#famille-table").on("click", ".js-delete-famille", loadForm);
    $("#modal-famille").on("submit", ".js-famille-delete-form", saveForm);
    $("#modal-famille").on("input", "#id_famille", valid);
   
  });
 