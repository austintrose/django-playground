from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models

class Person(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "people"

    def get_absolute_url(self):
        return reverse('people:person_detail', args=[str(self.id)])

    def __unicode__(self):
        return self.name
