# Generated by Django 3.0.3 on 2020-03-22 19:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0009_auto_20200321_0033'),
    ]

    operations = [
        migrations.DeleteModel(
            name='register',
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='myblog.post'),
        ),
    ]
