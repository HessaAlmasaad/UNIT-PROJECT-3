# Generated by Django 5.1.3 on 2024-12-02 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0003_project_roll"),
    ]

    operations = [
        migrations.RemoveField(model_name="project", name="roll",),
        migrations.AddField(
            model_name="project",
            name="file",
            field=models.FileField(blank=True, null=True, upload_to="uploads/"),
        ),
    ]