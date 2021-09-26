# Generated by Django 3.2.7 on 2021-09-26 19:00

from django.db import migrations, models
import portfolio.models.testimonials


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='Modified At')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Is Instance marked deleted')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Instance marked Active')),
                ('quote', models.CharField(max_length=64, verbose_name='Quote')),
                ('image', models.ImageField(blank=True, null=True, upload_to=portfolio.models.testimonials.upload_to, verbose_name='image')),
                ('review_name', models.CharField(max_length=64, verbose_name="Review's Name")),
                ('review', models.TextField(verbose_name='Review')),
                ('designation', models.CharField(blank=True, max_length=64, null=True, verbose_name='Designation')),
                ('organisation', models.CharField(blank=True, max_length=64, null=True, verbose_name='Organisation')),
            ],
            options={
                'verbose_name': 'Testimonial',
                'verbose_name_plural': 'Testimonials',
            },
        ),
    ]
