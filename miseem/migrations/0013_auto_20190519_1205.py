# Generated by Django 2.2.1 on 2019-05-19 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miseem', '0012_auto_20190519_1008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='absolute_score',
            field=models.IntegerField(choices=[(90, '9.0'), (51, '5.1'), (50, '5.0'), (42, '4.2'), (67, '6.7'), (18, '1.8'), (99, '9.9'), (33, '3.3'), (98, '9.8'), (19, '1.9'), (8, '0.8'), (69, '6.9'), (3, '0.3'), (57, '5.7'), (83, '8.3'), (52, '5.2'), (95, '9.5'), (61, '6.1'), (96, '9.6'), (79, '7.9'), (15, '1.5'), (53, '5.3'), (25, '2.5'), (35, '3.5'), (62, '6.2'), (45, '4.5'), (21, '2.1'), (73, '7.3'), (38, '3.8'), (39, '3.9'), (58, '5.8'), (30, '3.0'), (2, '0.2'), (4, '0.4'), (93, '9.3'), (87, '8.7'), (80, '8.0'), (49, '4.9'), (29, '2.9'), (65, '6.5'), (48, '4.8'), (66, '6.6'), (12, '1.2'), (36, '3.6'), (23, '2.3'), (86, '8.6'), (46, '4.6'), (16, '1.6'), (37, '3.7'), (91, '9.1'), (5, '0.5'), (1, '0.1'), (10, '1.0'), (31, '3.1'), (20, '2.0'), (43, '4.3'), (32, '3.2'), (92, '9.2'), (78, '7.8'), (9, '0.9'), (26, '2.6'), (7, '0.7'), (13, '1.3'), (22, '2.2'), (74, '7.4'), (100, '10.0'), (70, '7.0'), (76, '7.6'), (17, '1.7'), (68, '6.8'), (56, '5.6'), (59, '5.9'), (63, '6.3'), (88, '8.8'), (82, '8.2'), (71, '7.1'), (54, '5.4'), (60, '6.0'), (28, '2.8'), (6, '0.6'), (11, '1.1'), (72, '7.2'), (77, '7.7'), (84, '8.4'), (85, '8.5'), (94, '9.4'), (14, '1.4'), (81, '8.1'), (44, '4.4'), (47, '4.7'), (97, '9.7'), (75, '7.5'), (27, '2.7'), (40, '4.0'), (34, '3.4'), (24, '2.4'), (89, '8.9'), (64, '6.4'), (41, '4.1'), (55, '5.5')]),
        ),
        migrations.AlterField(
            model_name='answer',
            name='belong_to_type',
            field=models.IntegerField(choices=[(1, 'pointwise'), (2, 'pairwise'), (3, 'listwise')]),
        ),
    ]
