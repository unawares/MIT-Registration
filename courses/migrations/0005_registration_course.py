# Generated by Django 2.1.2 on 2018-10-27 08:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_speaker_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='course',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='registrations', to='courses.Course'),
            preserve_default=False,
        ),
    ]
