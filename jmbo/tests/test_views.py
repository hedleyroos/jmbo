from django.conf import settings
from django.core.management import call_command
from django.contrib.sites.models import Site
from django.test import TestCase
from django.urls import reverse

from photologue.models import PhotoSizeCache

from jmbo.models import ModelBase


class ViewsTestCase(TestCase):
    fixtures = ["sites.json"]

    @classmethod
    def setUpTestData(cls):
        super(ViewsTestCase, cls).setUpTestData()

        cls.obj = ModelBase.objects.create(title="title1")
        cls.obj.save()
        cls.obj.sites.set(Site.objects.all())
        cls.obj.publish()

        call_command("load_photosizes")
        PhotoSizeCache().reset()

    def test_detail_view(self):
        url = self.obj.get_absolute_url()
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.failUnless("""<div class="jmbo-detail jmbo-detail jmbo-modelbase-detail""" in response.content.decode("utf-8"))

    def test_list_view(self):
        url = reverse("jmbo:modelbase-list", args=["jmbo", "modelbase"])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.failUnless("""<div class="jmbo-list""" in response.content.decode("utf-8"))
