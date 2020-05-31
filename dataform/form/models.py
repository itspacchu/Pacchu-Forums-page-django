from django.db import models
from phone_field import PhoneField
from django import forms
import socket

class Snippet(models.Model):
    choices = [
        ('python','Python'),
        ('c','C'),
        ('c++','C++'),
        ('csharp','C#'),
        ('java','JAVA'),
        ('javascript','Javascript'),
        ('ruby','Ruby'),
        ('assembly','Assembly'),
        ('brainfuck','BrainFuck'),
        ('cobol','COBOL'),
        ('fotran','FOTRAN'),
        ('pascal','Pascal'),
        ('php','PHP'),
        ('basic','BASIC'),
        ('other','Other')
        ]

    name = models.CharField(
        max_length=100 ,
        verbose_name="Name"
        )

    rollno = models.CharField(
        max_length=10,
        verbose_name="Roll No"
        )

    sec = models.CharField(
        max_length=10,
        verbose_name="Class")

    phoneno = PhoneField(
        blank=True,
        verbose_name="Phone No"
        )

    languages = models.CharField(
        choices=choices,
        blank=True,
        max_length=200,
        verbose_name="Preferred Language"
        )

    email = models.EmailField(
        blank=True,
        default=' ',
        verbose_name="EMAIL"
        )

    githubusername = models.CharField(
        max_length=50,
        blank=True,
        verbose_name="Github Username"
        )

    githublink = models.URLField(
        blank=True,
        verbose_name="Github Profile")
    
    body = models.TextField(
        blank=True,
        default='Any Queries?',
        verbose_name="Suggestion"
        )

    user_ip = models.GenericIPAddressField(default = socket.gethostbyname(socket.gethostname()))

    def __str__(self):
        return self.name