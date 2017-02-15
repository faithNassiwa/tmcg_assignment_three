from django.test import TestCase
from models import Group


class TestGroup(TestCase):

    def setUp(self):
        Group.objects.create(uuid="5f05311e-8f81-4a67-a5b5-1501b6d6496a", name="Reporters", count=315)

    def test_get_number_of_contacts(self):
        group = Group.objects.first()
        self.assertEquals(group.get_number_of_contacts(), group.count)