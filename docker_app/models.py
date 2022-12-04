from django.db import models
from utils.randome_name import generate_randome_app_name


class ContainerizedApp(models.Model):
    container_name = models.CharField(max_length=250, null=False, blank=False)
    image_name = models.CharField(max_length=250, null=False, blank=False)
    envs = models.CharField(max_length=300, null=True, blank=True)
