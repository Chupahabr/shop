# Generated by Django 3.1.4 on 2021-01-14 09:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='brend',
            new_name='brand',
        ),
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.RemoveField(
            model_name='product',
            name='keep',
        ),
        migrations.AddField(
            model_name='product',
            name='age',
            field=models.TextField(choices=[('k', 'Kind'), ('a', 'Abuls'), ('o', 'Old')], default='Abuls', verbose_name='Возраст'),
        ),
        migrations.AddField(
            model_name='product',
            name='gender',
            field=models.TextField(choices=[('m', 'Male'), ('f', 'Female')], default='Male', verbose_name='Пол'),
        ),
        migrations.AddField(
            model_name='production_type',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='main.category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='production_type',
            name='p_type',
            field=models.CharField(max_length=50, verbose_name='Тип'),
        ),
    ]