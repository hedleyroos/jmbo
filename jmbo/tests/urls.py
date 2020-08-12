from django.conf.urls import include, url
from django.contrib import admin

from rest_framework import routers

from jmbo.views import ObjectDetail, ObjectList
from jmbo import api as jmbo_api
from jmbo import urls as jmbo_urls
from jmbo.tests import api as tests_api

admin.autodiscover()

router = routers.SimpleRouter()

jmbo_api.register(router)
tests_api.register(router)

urlpatterns = [
    url(r"^admin/", admin.site.urls),
    url(r'^api/(?P<version>(v1))/', include(router.urls)),
    url(r"^jmbo/", include(jmbo_urls, namespace="jmbo")),
    url(r"^comments/", include("django_comments.urls")),
    url(r"^likes/", include("likes.urls")),

    url(
        r"^tests/detail/(?P<slug>[\w-]+)/$",
        ObjectDetail.as_view(),
        name="tests-branchmodel-detail"
    ),

    url(
        r"^tests/detail/(?P<slug>[\w-]+)/$",
        ObjectDetail.as_view(),
        name="tests-leafmodel-detail"
    ),

    url(
        r"^tests/detail/(?P<category_slug>[\w-]+)/(?P<slug>[\w-]+)/$",
        ObjectDetail.as_view(),
        name="tests-leafmodel-categorized-detail"
    ),
]
