from django.db import models


class Subscriber(models.Model):
    name = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)


    class Meta:
        verbose_name_plural = "Subscribers"

    def __str__(self):
        return "%s %s" % (self.name, self.email)


