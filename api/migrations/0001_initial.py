# Generated by Django 3.2.5 on 2021-07-27 20:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('id', models.PositiveSmallIntegerField(primary_key=True, serialize=False)),
                ('capacity', models.PositiveSmallIntegerField(default=5)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('starts_at', models.DateTimeField()),
                ('ends_at', models.DateTimeField()),
                ('cancelled', models.BooleanField(default=False)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.room')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Catering',
            fields=[
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('Lunch1', models.PositiveSmallIntegerField(default=0)),
                ('Lunch2', models.PositiveSmallIntegerField(default=0)),
                ('BreakfastA', models.PositiveSmallIntegerField(default=0)),
                ('BreakfastB', models.PositiveSmallIntegerField(default=0)),
                ('WaterJar', models.PositiveSmallIntegerField(default=0)),
                ('CofeeJar', models.PositiveSmallIntegerField(default=0)),
                ('reservation', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.reservation')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]