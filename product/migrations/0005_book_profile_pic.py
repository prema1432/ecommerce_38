# Generated by Django 5.0.3 on 2024-03-06 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0004_alter_book_description"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="profile_pic",
            field=models.ImageField(blank=True, null=True, upload_to="profiles/"),
        ),
    ]
