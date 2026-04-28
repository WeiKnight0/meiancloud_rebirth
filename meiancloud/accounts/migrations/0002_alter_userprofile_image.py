from django.db import migrations, models

import accounts.models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="image",
            field=models.ImageField(
                blank=True,
                max_length=100,
                null=True,
                upload_to=accounts.models.user_directory_path,
                verbose_name="头像",
            ),
        ),
    ]
