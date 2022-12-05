from rest_framework import serializers


class BaseModelSerializer(serializers.ModelSerializer):

    id = serializers.CharField()

    def __init__(self, instance=None, data=..., **kwargs):
        self.set_model()
        super().__init__(instance, data, **kwargs)

    def set_model(self, model):
        self.Meta.model = model

    class Meta:
        exclude = ('is_deleted', 'updated_at', 'created_at')
