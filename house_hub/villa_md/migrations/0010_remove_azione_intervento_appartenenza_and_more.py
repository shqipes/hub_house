# Generated by Django 4.2.7 on 2023-11-30 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('villa_md', '0009_alter_mese_saldato_alter_orario_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='azione',
            name='intervento_appartenenza',
        ),
        migrations.AddField(
            model_name='azione',
            name='intervento_appartenenza',
            field=models.ManyToManyField(to='villa_md.intervento'),
        ),
    ]