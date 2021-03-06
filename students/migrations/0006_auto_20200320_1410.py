# Generated by Django 3.0.4 on 2020-03-20 06:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_auto_20200320_1351'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_dis', models.CharField(max_length=250, unique=True, verbose_name='type of disability')),
            ],
        ),
        migrations.AlterField(
            model_name='studentname',
            name='block',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='students.Block', verbose_name='section'),
        ),
        migrations.AddField(
            model_name='studentname',
            name='disability',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='students.Disability', verbose_name='child diagnosis'),
        ),
    ]
