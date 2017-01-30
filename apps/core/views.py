# -*- coding: utf-8 -*-
from django.conf import settings
from django.views.generic import TemplateView


class LandingPageTemplateView(TemplateView):
    """Site landing page."""

    template_name = 'core/landing_page.html'


class EducationTemplateView(TemplateView):
    """Displays educational background."""

    template_name = 'core/education.html'

    def get_context_data(self, *args, **kwargs):
        """Add map key."""
        context = super(EducationTemplateView, self).get_context_data(*args,
            **kwargs)
        context['MAP_API_KEY'] = settings.MAP_API_KEY
        return context


class ExperienceTemplateView(TemplateView):
    """Displays experiences."""

    template_name = 'core/experience.html'

    def get_context_data(self, *args, **kwargs):
        """Add map key."""
        context = super(ExperienceTemplateView, self).get_context_data(*args,
            **kwargs)
        context['MAP_API_KEY'] = settings.MAP_API_KEY
        return context


class AboutTemplateView(TemplateView):
    """Displays about page."""

    template_name = 'core/about.html'
