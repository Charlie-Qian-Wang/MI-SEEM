# Generated by Django 2.2 on 2019-05-11 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('miseem', '0003_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='absolute_score',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='answer',
            name='first',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='first_sentence', to='miseem.Sentence'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='answer',
            name='relative_score',
            field=models.IntegerField(choices=[(1, 'Win'), (0, 'Tie'), (-1, 'Lose')], default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='answer',
            name='second',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='second_sentence', to='miseem.Sentence'),
        ),
        migrations.AddField(
            model_name='answer',
            name='third',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='third_sentence', to='miseem.Sentence'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='belong_to_question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='miseem.Question'),
        ),
        migrations.AlterField(
            model_name='sentence',
            name='belong_to_question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='miseem.Question'),
        ),
        migrations.AlterField(
            model_name='sentence',
            name='belong_to_system',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='miseem.System'),
        ),
    ]
