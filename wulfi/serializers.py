from rest_framework.serializers import ModelSerializer, StringRelatedField 

from .models import Profile, Tag, Post, Project



class TagSerializer(ModelSerializer):
    
    name = StringRelatedField(read_only=True)
    
    class Meta:
        model = Tag
        fields = "__all__"
        # exclude = ('watchlist',)
        
class PostSerializer(ModelSerializer):
    author = StringRelatedField(read_only=True)
    tags = TagSerializer(read_only=True, many=True)
   
    class Meta:
        model = Post 
        fields = '__all__'