# Generated by Django 4.2.7 on 2024-01-03 02:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0009_tag"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="tag",
            options={"ordering": ["name"]},
        ),
        migrations.AddIndex(
            model_name="tag",
            index=models.Index(fields=["name"], name="blog_tag_name_43b6ed_idx"),
        ),
    ]