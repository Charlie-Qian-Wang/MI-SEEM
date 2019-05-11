# Generated by Django 2.2 on 2019-05-11 07:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('miseem', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('standard', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='sentence',
            name='belong_to_question',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='miseem.Question'),
            preserve_default=False,
        ),
    ]
