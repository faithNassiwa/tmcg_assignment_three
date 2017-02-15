from __future__ import unicode_literals
from django.db import models
from temba_client.v2 import TembaClient


client = TembaClient('rapidpro.io', 'your-api-token'')
groups = client.get_groups().all()


class GroupManager(models.Manager):
    def create_group(self, uuid, name, count):
        return self.create(uuid=uuid, name=name, count=count)


class Group(models.Model):
    uuid = models.CharField(max_length=50, blank=False)
    name = models.CharField(max_length=50, blank= False)
    count = models.IntegerField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = GroupManager()

    def __unicode__(self):
        return self.name

    def get_number_of_contacts(self):
        return self.count


for g in groups:
    Group.objects.create_group(g.uuid, g.name, g.count)





