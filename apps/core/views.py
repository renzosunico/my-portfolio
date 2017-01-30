# -*- coding: utf-8 -*-
from django.views.generic import TemplateView


class LandingPageTemplateView(TemplateView):
    """Site landing page."""

    template_name = 'core/landing_page.html'


class EducationTemplateView(TemplateView):
    """Displays educational background."""

    template_name = 'core/education.html'


class ExperienceTemplateView(TemplateView):
    """Displays experiences."""

    template_name = 'core/experience.html'
