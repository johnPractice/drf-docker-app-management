from django.db import models
from utils.base_model import BaseModel
from utils.http_exception import NotFoundItem


class ContainerizedApp(BaseModel):
    container_name = models.CharField(max_length=250, null=False, blank=False)
    image_name = models.CharField(max_length=250, null=False, blank=False)
    envs = models.CharField(max_length=300, null=True, blank=True)

    @staticmethod
    def get_with_id_or_name(pk):
        container_instance = ContainerizedApp.retrive_by_id(id=pk)
        if container_instance is None:
            try:
                container_instance = ContainerizedApp.objects.get(
                    container_name=pk)
            except ContainerizedApp.DoesNotExist:
                raise NotFoundItem()

        return container_instance
