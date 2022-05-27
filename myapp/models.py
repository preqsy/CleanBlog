from django.db import models


class Home(models.Model):
    PRECIOUS_OBINNA = 'Precious Obinna'
    OHANYERE_PRECIOUS = 'Ohanyere Precious'
    JUDE_OHANYERE = 'Jude Ohanyere'

    AUTHOR_CHOICE = (
        (PRECIOUS_OBINNA, 'Precious Obinna'),
        (OHANYERE_PRECIOUS, 'Ohanyere Precious'),
        (JUDE_OHANYERE, 'Jude Ohanyere')

    )
    title = models.CharField(max_length=1000)
    body = models.TextField()
    author = models.CharField(max_length=100, choices=AUTHOR_CHOICE)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.PositiveIntegerField()
    message = models.TextField()

    def __str__(self):
        return self.name
