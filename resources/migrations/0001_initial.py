# Generated by Django 3.0.10 on 2021-04-03 09:41

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('character_name', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_out_date', models.DateField(default=django.utils.timezone.now)),
                ('return_date', models.DateField(blank=True, null=True)),
                ('status', models.CharField(choices=[('D', 'Due'), ('R', 'Returned')], default='D', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('name', models.CharField(max_length=255, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('place_name', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('subject_name', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('revision', models.PositiveIntegerField()),
                ('publish_date', models.DateTimeField(blank=True, null=True)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='resources.Author')),
                ('characters', models.ManyToManyField(blank=True, to='resources.Character')),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='resources.Location')),
                ('places', models.ManyToManyField(blank=True, to='resources.Place')),
                ('subjects', models.ManyToManyField(blank=True, to='resources.Subject')),
            ],
        ),
    ]
