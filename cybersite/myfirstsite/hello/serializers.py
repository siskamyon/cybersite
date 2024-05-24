from rest_framework import serializers
from rest_framework.response import Response
from .models import Post


#class PostModel:
#    def __init__(self, title, content):
#        self.title = title
#        self.content = content


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

#    title = serializers.CharField(max_length=255)
#    content = serializers.CharField()
#    img = serializers.ImageField(read_only=True)
#    date = serializers.DateTimeField(read_only=True)
#    cat_id = serializers.IntegerField()
#    author_id = serializers.IntegerField()
#
#    def create(self, validated_data):
#        return Post.objects.create(**validated_data)
#    
#    def update(self, instance, validated_data):
#        instance.title = validated_data.get("title", instance.title)
#        instance.content = validated_data.get("content", instance.content)
#        instance.img = validated_data.get("img", instance.img)
#        instance.cat_id = validated_data.get("cat_id", instance.cat_id)
#        instance.author_id = validated_data.get("author_id", instance.author_id)
#        instance.save()
#        return instance
#    
#    def put(self, request, *args, **kwargs):
#        pk = kwargs.get("pk", None)
#        if not pk:
#            return Response({"error": "Method PUT not allowed"})
#        
#        try:
#            instance = Post.objects.get(pk=pk)
#        except:
#            return Response({"error": "Object does not exists"})
#        
#        serializer = PostSerializer(data=request.data, instance=instance)
#        serializer.is_valid(raise_exception=True)
#        serializer.save()
#        return Response({"post": serializer.data})
#
#    def delete(self, request, *args, **kwargs):
#        pk = kwargs.get('pk', None)
#        if not pk:
#            return Response({"error": "Method DELETE not allowed"})
#        try:
#            record = Post.objects.filter(pk=pk)
#            record.delete()
#        except:
#            return Response({"error": "Object does not exists"})
#
#        return Response({"post": "delete post " + str(pk)})
    
        