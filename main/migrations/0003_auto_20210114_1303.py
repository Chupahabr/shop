# Generated by Django 3.1.4 on 2021-01-14 10:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210114_1235'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='brand_en',
            field=models.CharField(max_length=50, null=True, verbose_name='Бренд'),
        ),
        migrations.AddField(
            model_name='brand',
            name='brand_ru',
            field=models.CharField(max_length=50, null=True, verbose_name='Бренд'),
        ),
        migrations.AddField(
            model_name='category',
            name='category_en',
            field=models.CharField(max_length=50, null=True, verbose_name='Категории'),
        ),
        migrations.AddField(
            model_name='category',
            name='category_ru',
            field=models.CharField(max_length=50, null=True, verbose_name='Категории'),
        ),
        migrations.AddField(
            model_name='product',
            name='about_en',
            field=models.TextField(null=True, verbose_name='Обо мне'),
        ),
        migrations.AddField(
            model_name='product',
            name='about_ru',
            field=models.TextField(null=True, verbose_name='Обо мне'),
        ),
        migrations.AddField(
            model_name='product',
            name='brand_en',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='main.brand', verbose_name='Бренд'),
        ),
        migrations.AddField(
            model_name='product',
            name='brand_ru',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='main.brand', verbose_name='Бренд'),
        ),
        migrations.AddField(
            model_name='product',
            name='info_en',
            field=models.TextField(null=True, verbose_name='Информация'),
        ),
        migrations.AddField(
            model_name='product',
            name='info_ru',
            field=models.TextField(null=True, verbose_name='Информация'),
        ),
        migrations.AddField(
            model_name='product',
            name='prod_name_en',
            field=models.CharField(max_length=50, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='product',
            name='prod_name_ru',
            field=models.CharField(max_length=50, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='product',
            name='production_type_en',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='main.production_type', verbose_name='Тип продукта'),
        ),
        migrations.AddField(
            model_name='product',
            name='production_type_ru',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='main.production_type', verbose_name='Тип продукта'),
        ),
        migrations.AddField(
            model_name='product',
            name='size_and_cut_en',
            field=models.TextField(null=True, verbose_name='Размер и крой'),
        ),
        migrations.AddField(
            model_name='product',
            name='size_and_cut_ru',
            field=models.TextField(null=True, verbose_name='Размер и крой'),
        ),
        migrations.AddField(
            model_name='product',
            name='sport_type_en',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='main.sport_type', verbose_name='Вид спорта'),
        ),
        migrations.AddField(
            model_name='product',
            name='sport_type_ru',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='main.sport_type', verbose_name='Вид спорта'),
        ),
        migrations.AddField(
            model_name='product',
            name='upkeep_en',
            field=models.TextField(null=True, verbose_name='Уход'),
        ),
        migrations.AddField(
            model_name='product',
            name='upkeep_ru',
            field=models.TextField(null=True, verbose_name='Уход'),
        ),
        migrations.AddField(
            model_name='production_type',
            name='p_type_en',
            field=models.CharField(max_length=50, null=True, verbose_name='Тип'),
        ),
        migrations.AddField(
            model_name='production_type',
            name='p_type_ru',
            field=models.CharField(max_length=50, null=True, verbose_name='Тип'),
        ),
        migrations.AddField(
            model_name='sport_type',
            name='sport_type_en',
            field=models.CharField(max_length=50, null=True, verbose_name='Вид спорта'),
        ),
        migrations.AddField(
            model_name='sport_type',
            name='sport_type_ru',
            field=models.CharField(max_length=50, null=True, verbose_name='Вид спорта'),
        ),
    ]
