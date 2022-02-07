# Generated by Django 3.2.8 on 2021-11-15 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_alter_stock_issue_to'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='distinations',
            name='societe',
        ),
        migrations.AlterField(
            model_name='distinations',
            name='nom_dis',
            field=models.CharField(max_length=50, unique=True, verbose_name='Emplacement'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='issue_to',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.distinations', verbose_name='Emplacement'),
        ),
    ]
