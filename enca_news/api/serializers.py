from rest_framework import serializers
from rest_framework.serializers import HyperlinkedIdentityField
from .models import News, MainNews

# Serializers define the API representation.
class NewsSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = News
        fields = (
            'them_images',
            'body_title',
            'summary',
            'links'
        )

class MainNewsSerializer(serializers.HyperlinkedModelSerializer):
 
    class Meta:
        model = MainNews
        fields = (
            'lead_content',
            'title',
            'img',
            'image_caption'
        )

