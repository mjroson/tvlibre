from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Profile



class ProfileSerializer(serializers.ModelSerializer):
    #phones = PhoneSerializer(many=True)
    #user = UserProfileSerializer()
    #image = serializers.ImageField(allow_empty_file=True, use_url=True, read_only=True)

    class Meta:
        model = Profile
        depth = 2
        fields = ('image', 'birth_date',  'id')
        read_only_fields = ('id',)


    # def update(self, instance, validated_data):
    #     user_data = validated_data.get('user', instance.user)
    #     request = self.context.get('request', None)
    #     user_serializer = UserProfileSerializer()
    #     instance.user = user_serializer.update(instance=request.user, validated_data=user_data)
    #
    #     phones_data = validated_data.get('phones', [])
    #     if phones_data:
    #         Phone.objects.filter(userProfile=instance).delete()
    #         for phone in phones_data:
    #             p = Phone()
    #             p.userProfile = instance
    #             p.number= int(phone.get('number', 0))
    #             p.type = phone.get('type', 'TEL')
    #             p.save()
    #
    #     instance.birth_date = validated_data.get('birth_date', instance.birth_date)
    #
    #     instance.save()
    #
    #     return instance



class UserAuthenticationSerializer(serializers.ModelSerializer):
    #profile = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        depth = 2
        fields = '__all__'


    #def get_profile(self, obj):
        #return ProfileSerializer(instance=obj.profile).data