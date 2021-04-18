# Generated by Django 2.2.5 on 2021-04-18 22:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0002_auto_20210416_1049'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='survey',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='survey',
            name='a_username',
        ),
        migrations.RemoveField(
            model_name='survey',
            name='u_username',
        ),
        migrations.AlterField(
            model_name='analysis',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='analysis',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='analyst',
            name='email',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='analyst',
            name='name',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='analyst',
            name='password',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='call',
            name='ask',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='call',
            name='bid',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='call',
            name='premium',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='exchange',
            name='exchange_timezone',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='histogram_entry',
            name='value',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='put',
            name='ask',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='put',
            name='bid',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='put',
            name='premium',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='current_value',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='dividend_amount',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='exchange_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='test_app.Exchange'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='name',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='value_history',
            name='value',
            field=models.FloatField(null=True),
        ),
        migrations.DeleteModel(
            name='Stock_Analysis',
        ),
        migrations.DeleteModel(
            name='Survey',
        ),
    ]
