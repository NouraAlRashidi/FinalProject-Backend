# Generated by Django 2.1.1 on 2018-09-24 14:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('final', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidate',
            name='email',
        ),
        migrations.RemoveField(
            model_name='candidate',
            name='employer_name',
        ),
        migrations.AddField(
            model_name='candidate',
            name='candidate_email',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='candidate',
            name='employers',
            field=models.ManyToManyField(related_name='candidates', to='final.Employer'),
        ),
    ]
