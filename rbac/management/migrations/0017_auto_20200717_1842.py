# Generated by Django 2.2.4 on 2020-07-17 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("management", "0016_make_bridge_for_migration")]

    operations = [
        migrations.RenameField(model_name="permission", old_name="app", new_name="application"),
        migrations.RenameField(model_name="permission", old_name="resource", new_name="resource_type"),
        migrations.RenameField(model_name="permission", old_name="operation", new_name="verb"),
    ]
