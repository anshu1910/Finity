# Generated by Django 4.1.7 on 2023-03-28 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='users',
            fields=[
                ('UserId', models.AutoField(primary_key=True, serialize=False)),
                ('FirstName', models.CharField(max_length=100)),
                ('LastName', models.CharField(max_length=100)),
                ('EmailId', models.CharField(max_length=100)),
                ('MobileNumber', models.CharField(max_length=100)),
            ],
        ),
    ]