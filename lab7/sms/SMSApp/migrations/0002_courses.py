# Generated by Django 2.0.4 on 2018-04-05 19:02

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('SMSApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('credit', models.IntegerField(default=3)),
                ('isActive', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
