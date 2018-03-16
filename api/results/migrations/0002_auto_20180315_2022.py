# Generated by Django 2.0.3 on 2018-03-15 20:22

from django.db import migrations


def generate_results(apps, schema_editor) -> None:
    GeneticResult = apps.get_model('results', 'GeneticResult')


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(generate_results)
    ]