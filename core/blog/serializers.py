from rest_framework import serializers
from .models import Post, Category
from .models import Post
from comment.models import Comment

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Post
        fields = '__all__'


class CommentMiniSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Comment
        fields = ['id', 'text', 'user', 'created_at']


class PostSerializer(serializers.ModelSerializer):
    comments = CommentMiniSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'content',
            'category',
            'author',
            'created_at',
            'comments'
        ]