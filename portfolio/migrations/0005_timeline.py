# Generated by Django 3.2.7 on 2021-10-05 18:22

from django.db import migrations, models
import portfolio.models.timeline


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='Timeline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='Modified At')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Is Instance marked deleted')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Instance marked Active')),
                ('title', models.CharField(max_length=64, verbose_name='Timeline title')),
                ('image', models.ImageField(upload_to=portfolio.models.timeline.upload_to, verbose_name='Image')),
                ('text', models.TextField(blank=True, null=True, verbose_name='Text')),
                ('from_date', models.DateField(blank=True, null=True, verbose_name='From date')),
                ('to_date', models.DateField(blank=True, null=True, verbose_name='To date')),
            ],
            options={
                'verbose_name': 'Timeline',
                'verbose_name_plural': 'Timelines',
            },
        ),
    ]
