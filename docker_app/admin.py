from django.contrib import admin

from docker_app.models import ContainerizedApp


@admin.register(ContainerizedApp)
class ContainerizedAppAdmin(admin.ModelAdmin):
    list_display = ('id', 'container_name', 'created_at')
