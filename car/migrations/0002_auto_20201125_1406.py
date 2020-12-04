# Generated by Django 3.1.2 on 2020-11-25 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TagModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'tags',
            },
        ),
        migrations.AddField(
            model_name='carmodel',
            name='tags',
            field=models.ManyToManyField(related_name='car', to='car.TagModel'),
        ),
    ]