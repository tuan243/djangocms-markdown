from django.db import models

from cms.models import CMSPlugin


class Markdown(CMSPlugin):
    body = models.TextField()
