from django.db import models

# Create your models here.

class Password(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.username


# brendan
# brendanranker1

# luka
# lukaranker1


