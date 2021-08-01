from django.db import models
class events(models.Model):
    Event_name=models.CharField(max_length=100)
    Date=models.DateField(blank=True, null=True)
    Time=models.DurationField()
    Location=models.CharField(max_length=100)


    def __str__(self):
        return self.Event_name
# Create your models here.
