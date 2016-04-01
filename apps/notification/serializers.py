from rest_framework import serializers

from .models import Notification

from apps.program.serializers import EpisodeSerializer

FAVORITE_CONTENT_TYPE_CHOICES = (
    7, 'Program',
    8, 'Episode'
)

class NotificationSerializer(serializers.ModelSerializer):
    obj = serializers.SerializerMethodField()
    #target_content_type = serializers.IntegerField(choices=FAVORITE_CONTENT_TYPE_CHOICES)
    class Meta:
        model = Notification
        readonly_fields = ('id', 'created', 'user', 'obj')
        #fields = ('target_content_type', 'target_object_id', 'obj')

    def get_obj(self, instance):
        #TODO: Set dynamic instance
        return EpisodeSerializer(instance=instance.obj).data