from rest_framework import serializers
from django.contrib.auth.models import User
from core.models import (
    FAQ,
    Core,
    TypeOfService,
    AreaOfDuty,
    Unit,
    Popup,
    Tag,
    AreaOfActivity,
    WebsiteInformations,
    SocialMedia,
    )

class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = '__all__'
        read_only_fields = ['author', 'created_at', 'updated_at', 'published_at']

class CoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Core
        fields = '__all__'
        read_only_fields = ['author', 'created_at', 'updated_at', 'published_at']

class TypeOfServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeOfService
        fields = '__all__'
        read_only_fields = ['author', 'created_at', 'updated_at', 'published_at']

class AreaOfDutySerializer(serializers.ModelSerializer):
    class Meta:
        model = AreaOfDuty
        fields = '__all__'
        read_only_fields = ['author', 'created_at', 'updated_at', 'published_at']

class UnitSerializer(serializers.ModelSerializer):
    core = CoreSerializer(read_only=True)
    tipo_de_atendimento = TypeOfServiceSerializer(read_only=True)
    area_de_atribuicao = AreaOfDutySerializer(read_only=True)

    class Meta:
        model = Unit
        fields = '__all__'
        read_only_fields = ['author', 'created_at', 'updated_at', 'published_at']

class PopupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Popup
        fields = '__all__'
        read_only_fields = ['click', 'visualization', 'author', 'created_at', 'updated_at', 'published_at']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
        read_only_fields = ['times_used', 'author', 'created_at', 'updated_at', 'published_at']

class AreaOfActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = AreaOfActivity
        fields = '__all__'
        read_only_fields = ['author', 'created_at', 'updated_at', 'published_at'] 

class WebsiteInformationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebsiteInformations
        fields = '__all__'
        read_only_fields = ['author', 'created_at', 'updated_at', 'published_at']

class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = '__all__'
        read_only_fields = ['author', 'created_at', 'updated_at', 'published_at']