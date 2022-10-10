# Generated by Django 3.2 on 2022-10-10 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OrderEvaluate',
            fields=[
                ('orderevaluate_id', models.AutoField(primary_key=True, serialize=False)),
                ('orderevaluate_part', models.CharField(max_length=32)),
                ('orderevaluate_date', models.DateTimeField(auto_now_add=True, db_index=True)),
            ],
        ),
    ]
