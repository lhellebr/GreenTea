from datetime import timedelta

from django.db import models

from apps.core.utils.date_helpers import TZDateTimeField, currentDate


class Performance(models.Model):
    label = models.CharField(max_length=32, blank=True, null=True)
    name = models.CharField(max_length=64)
    description = models.TextField(blank=True)
    date_create = TZDateTimeField(default=currentDate)
    duration = models.FloatField()
    exitcode = models.IntegerField()

    def __unicode__(self):
        return self.name

    def get_duration(self):
        return unicode(timedelta(seconds=self.duration))
