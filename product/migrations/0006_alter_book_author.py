# Generated by Django 5.0.3 on 2024-03-07 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0005_book_profile_pic"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="author",
            field=models.CharField(max_length=5),
        ),
    ]
