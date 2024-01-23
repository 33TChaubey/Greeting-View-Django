from django.db import models

class GreetingLog(models.Model):
    greeting = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.greeting} at {self.timestamp}'
