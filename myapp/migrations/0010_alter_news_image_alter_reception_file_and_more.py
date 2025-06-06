# Generated by Django 5.1.6 on 2025-05-25 10:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_news_reception_teacher_yunalishlar_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/imgs/news/'),
        ),
        migrations.AlterField(
            model_name='reception',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='static/files/reception/'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='static/imgs/teachers/'),
        ),
        migrations.AlterField(
            model_name='yunalishlar',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/imgs/yunalishlar/'),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('passport', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('yunalish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.yunalishlar')),
            ],
        ),
    ]
