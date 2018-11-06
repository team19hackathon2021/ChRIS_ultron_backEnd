# Generated by Django 2.0.7 on 2018-11-01 20:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0006_auto_20181005_1702'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tagging',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feeds.Feed')),
            ],
        ),
        migrations.RemoveField(
            model_name='tag',
            name='feed',
        ),
        migrations.AddField(
            model_name='tagging',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feeds.Tag'),
        ),
        migrations.AddField(
            model_name='tag',
            name='feeds',
            field=models.ManyToManyField(related_name='tags', through='feeds.Tagging', to='feeds.Feed'),
        ),
        migrations.AlterUniqueTogether(
            name='tagging',
            unique_together={('feed', 'tag')},
        ),
    ]
