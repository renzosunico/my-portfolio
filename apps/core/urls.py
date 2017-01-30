# -*- coding: utf-8 -*-
from django.conf.urls import url
from core.views import LandingPageTemplateView
from core.views import EducationTemplateView
from core.views import ExperienceTemplateView
from core.views import AboutTemplateView

urlpatterns = [
    url(r'^$', LandingPageTemplateView.as_view(), name='landing'),
    url(r'^educations/$', EducationTemplateView.as_view(), name='educations'),
    url(r'^experiences/$', ExperienceTemplateView.as_view(),
        name='experiences'),
    url(r'^about/$', AboutTemplateView.as_view(), name='about')
]
