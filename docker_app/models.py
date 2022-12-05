from django.db import models
from utils.base_model import BaseModel


class ContainerizedApp(BaseModel):
    container_name = models.CharField(max_length=250, null=False, blank=False)
    image_name = models.CharField(max_length=250, null=False, blank=False)
    envs = models.CharField(max_length=300, null=True, blank=True)
