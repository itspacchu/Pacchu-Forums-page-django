# Generated by Django 3.0.6 on 2020-06-01 03:26

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0009_auto_20200531_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snippet',
            name='body',
            field=models.TextField(blank=True, verbose_name='I would like to ...'),
        ),
        migrations.AlterField(
            model_name='snippet',
            name='email',
            field=models.EmailField(blank=True, default=' ', help_text='senpai.awesome@kawaii.com', max_length=254, verbose_name='EMAIL'),
        ),
        migrations.AlterField(
            model_name='snippet',
            name='githublink',
            field=models.URLField(blank=True, help_text='https://github.com/itspacchu', verbose_name='Github Profile'),
        ),
        migrations.AlterField(
            model_name='snippet',
            name='githubusername',
            field=models.CharField(blank=True, help_text='itspacchu', max_length=50, verbose_name='Github Username'),
        ),
        migrations.AlterField(
            model_name='snippet',
            name='languages',
            field=models.CharField(blank=True, choices=[('python', 'Python'), ('c', 'C'), ('c++', 'C++'), ('csharp', 'C#'), ('java', 'JAVA'), ('javascript', 'Javascript'), ('ruby', 'Ruby'), ('assembly', 'Assembly'), ('brainfuck', 'BrainFuck'), ('cobol', 'COBOL'), ('fotran', 'FOTRAN'), ('pascal', 'Pascal'), ('php', 'PHP'), ('basic', 'BASIC'), ('other', 'Other')], max_length=200, verbose_name='Preferred Language'),
        ),
        migrations.AlterField(
            model_name='snippet',
            name='name',
            field=models.CharField(help_text="C'est Pacchu", max_length=100, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='snippet',
            name='phoneno',
            field=phone_field.models.PhoneField(blank=True, help_text='9876543217', max_length=31, verbose_name='Phone No'),
        ),
        migrations.AlterField(
            model_name='snippet',
            name='rollno',
            field=models.CharField(help_text='18AG1A0420', max_length=10, verbose_name='Roll No'),
        ),
        migrations.AlterField(
            model_name='snippet',
            name='sec',
            field=models.CharField(help_text='II ECE B', max_length=10, verbose_name='Class'),
        ),
    ]
