from django.db import models
from phone_field import PhoneField
from django import forms
import socket
from phonenumber_field.modelfields import PhoneNumberField

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
        verbose_name="Name",
        help_text="C'est Pacchu"
        )

    rollno = models.CharField(
        max_length=10,
        verbose_name="Roll No",
        help_text="18AG1A0420"
        )

    sec = models.CharField(
        max_length=10,
        verbose_name="Class",
        help_text="II ECE B"
        )


    phoneno = PhoneNumberField(help_text="+919876543210")

    languages = models.CharField(
        choices=choices,
        blank=True,
        max_length=200,
        default="other",
        verbose_name="Preferred Language"
        )

    email = models.EmailField(
        blank=True,
        default=' ',
        verbose_name="Email Address",
        help_text="senpai.awesome@kawaii.jp"

        )

    githubusername = models.CharField(
        max_length=50,
        blank=True,
        verbose_name="Github Username",
        help_text="itspacchu"
        )

    githublink = models.URLField(
        blank=True,
        verbose_name="Github Profile",
        help_text="https://github.com/itspacchu"
    )
    
    body = models.TextField(
        blank=True,
        verbose_name="Why do you want to join",
        help_text="I would love to ..."
        )

    user_ip = models.GenericIPAddressField(default = socket.gethostbyname(socket.gethostname()))

    def __str__(self):
        return self.name