# Generated by Django 3.0.6 on 2020-05-22 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shameem', '0004_delete_language_skill'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language_skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.IntegerField(default=0)),
                ('language', models.CharField(default='', max_length=20)),
                ('knowledge_in_percentage', models.IntegerField(default=0)),
            ],
        ),
    ]