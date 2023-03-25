from rest_framework import serializers

from posts.models import Post


class CreatePostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('title', 'text', 'created_by')
        extra_kwargs = {
            'created_by': {'required': False},
        }

    def validate(self, attrs):
        request = self.context.get('request', None)
        if request:
            user = request.user
            attrs['created_by'] = user
            return attrs
        raise serializers.ValidationError({
            'detail': 'User not found.'
        })


class ListPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'text', 'created_by', 'created_date')


class PostAnalyticsSerializer(serializers.Serializer):
    created_date = serializers.DateField(read_only=True)
    likes_count = serializers.IntegerField(read_only=True)


