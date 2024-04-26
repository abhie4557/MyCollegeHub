# Generated by Django 5.0.4 on 2024-04-26 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PDFDocument',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('pdf_file', models.FileField(upload_to='pdfs/')),
            ],
        ),
    ]