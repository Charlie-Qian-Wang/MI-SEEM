# Generated by Django 2.2 on 2019-05-11 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miseem', '0006_auto_20190511_0910'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='frequence',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sentence',
            name='frequence',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='system',
            name='frequence',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='answer',
            name='absolute_score',
            field=models.FloatField(choices=[(7.7, '7.7'), (6.3, '6.3'), (10.0, '10.0'), (5.4, '5.4'), (7.6, '7.6'), (7.8, '7.8'), (9.8, '9.8'), (4.9, '4.9'), (8.9, '8.9'), (4.5, '4.5'), (3.4, '3.4'), (6.7, '6.7'), (7.4, '7.4'), (6.2, '6.2'), (2.1, '2.1'), (1.1, '1.1'), (2.0, '2.0'), (5.6, '5.6'), (8.8, '8.8'), (3.1, '3.1'), (6.8, '6.8'), (2.9, '2.9'), (1.4, '1.4'), (4.4, '4.4'), (9.1, '9.1'), (3.2, '3.2'), (3.3, '3.3'), (7.5, '7.5'), (1.2, '1.2'), (8.1, '8.1'), (0.4, '0.4'), (9.3, '9.3'), (0.8, '0.8'), (4.0, '4.0'), (5.2, '5.2'), (7.2, '7.2'), (4.2, '4.2'), (1.6, '1.6'), (6.0, '6.0'), (1.9, '1.9'), (0.9, '0.9'), (6.6, '6.6'), (8.4, '8.4'), (2.6, '2.6'), (8.0, '8.0'), (9.4, '9.4'), (3.7, '3.7'), (3.6, '3.6'), (7.0, '7.0'), (2.2, '2.2'), (1.8, '1.8'), (9.6, '9.6'), (2.3, '2.3'), (0.6, '0.6'), (4.1, '4.1'), (6.1, '6.1'), (9.2, '9.2'), (2.4, '2.4'), (6.5, '6.5'), (5.9, '5.9'), (5.0, '5.0'), (4.7, '4.7'), (8.5, '8.5'), (1.5, '1.5'), (8.7, '8.7'), (9.9, '9.9'), (1.0, '1.0'), (2.8, '2.8'), (3.9, '3.9'), (0.5, '0.5'), (3.0, '3.0'), (9.5, '9.5'), (8.6, '8.6'), (9.7, '9.7'), (5.5, '5.5'), (1.7, '1.7'), (7.1, '7.1'), (5.3, '5.3'), (4.6, '4.6'), (3.8, '3.8'), (0.1, '0.1'), (2.7, '2.7'), (8.2, '8.2'), (4.8, '4.8'), (6.4, '6.4'), (2.5, '2.5'), (0.2, '0.2'), (3.5, '3.5'), (5.7, '5.7'), (6.9, '6.9'), (5.1, '5.1'), (0.3, '0.3'), (0.7, '0.7'), (9.0, '9.0'), (4.3, '4.3'), (8.3, '8.3'), (1.3, '1.3'), (7.3, '7.3'), (5.8, '5.8'), (7.9, '7.9')]),
        ),
    ]
