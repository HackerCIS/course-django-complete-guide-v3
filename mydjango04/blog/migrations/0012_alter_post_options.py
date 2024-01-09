# Generated by Django 4.2.7 on 2024-01-03 08:16

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0011_accesslog_created_at_accesslog_updated_at_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="post",
            options={
                "permissions": [("view_premium_post", "프리미엄 컨텐츠를 볼 수 있음")],
                "verbose_name": "포스팅",
                "verbose_name_plural": "포스팅 목록",
            },
        ),
    ]