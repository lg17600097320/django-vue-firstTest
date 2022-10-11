# Generated by Django 3.1.3 on 2022-08-17 03:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_auto_20220816_1635'),
    ]

    operations = [
        migrations.CreateModel(
            name='Avatar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.ImageField(upload_to='avatar/%Y%m%d')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='avatar',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='articles', to='article.avatar'),
        ),
    ]
