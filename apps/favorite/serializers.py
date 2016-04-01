from rest_framework import serializers

from .models import Favorite

from apps.program.serializers import ProgramSerializer

FAVORITE_CONTENT_TYPE_CHOICES = (
    7, 'Program',
    8, 'Episode'
)

class FavoriteSerializer(serializers.ModelSerializer):
    obj = serializers.SerializerMethodField()
    #target_content_type = serializers.IntegerField(choices=FAVORITE_CONTENT_TYPE_CHOICES)
    class Meta:
        model = Favorite
        readonly_fields = ('id', 'timestamp', 'user', 'obj')
        fields = ('target_content_type', 'target_object_id', 'obj')

    def get_obj(self, instance):
        #TODO: Set dynamic instance
        return ProgramSerializer(instance=instance.target).data