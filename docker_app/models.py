from django.db import models
from utils.randome_name import generate_randome_app_name


class ContainerizedApp(models.Model):
    app_name = models.CharField(
        max_length=250, default=generate_randome_app_name())
    image_name = models.CharField(max_length=250, null=False, blank=False)
    # run_command = models.cha
