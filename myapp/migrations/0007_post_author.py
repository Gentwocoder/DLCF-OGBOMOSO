# Generated by Django 4.1.2 on 2022-10-22 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0006_post"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="author",
            field=models.CharField(default="priceless jewel", max_length=100),
            preserve_default=False,
        ),
    ]