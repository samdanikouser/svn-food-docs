# Generated by Django 5.0.1 on 2024-10-13 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('haccp', '0002_alter_haccpbackburnerfreezer_corrective_action_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssignUsers',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='CorrectiveAction',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], max_length=10, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='HaccpAdminData',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('storage_location', models.CharField(max_length=200)),
                ('sub_storage_location', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('used_for', models.CharField(max_length=200)),
                ('assign_task_to', models.CharField(max_length=200)),
                ('repeat_every', models.IntegerField()),
                ('repeat_frequency', models.CharField(max_length=200)),
                ('time_on', models.JSONField()),
                ('min_temp', models.FloatField()),
                ('max_temp', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('assign_verifier', models.ManyToManyField(to='haccp.assignusers')),
                ('corrective_action', models.ManyToManyField(to='haccp.correctiveaction')),
            ],
        ),
        migrations.DeleteModel(
            name='HaccpBackBurnerFoodCooking',
        ),
        migrations.DeleteModel(
            name='HaccpBackBurnerFoodCooling',
        ),
        migrations.DeleteModel(
            name='HaccpBackBurnerFoodReheating',
        ),
        migrations.DeleteModel(
            name='HaccpBackBurnerFreezer',
        ),
        migrations.DeleteModel(
            name='HaccpBackBurnerFridge',
        ),
        migrations.DeleteModel(
            name='HaccpBackBurnerSanitization',
        ),
    ]
