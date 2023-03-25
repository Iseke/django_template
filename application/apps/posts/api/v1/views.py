from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import ListAPIView

from .filters import PostAnalyticsFilter
from .serializers import CreatePostSerializer, ListPostSerializer, PostAnalyticsSerializer
from posts.models import Post, PostLikes


class PostAnalyticsView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = PostAnalyticsSerializer
    queryset = Post.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_class = PostAnalyticsFilter

    def list(self, request, *args, **kwargs):
        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
        queryset = PostLikes.objects.filter(created_date__gte=date_from, created_date__lte=date_to).extra({'created_date' : "date(created_date)"}).values('created_date').annotate(likes_count=Count('id'))
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)



class PostViewSet(GenericViewSet, ListModelMixin, CreateModelMixin):
    permission_classes = (IsAuthenticated,)
    serializer_class = CreatePostSerializer
    queryset = Post.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return ListPostSerializer
        elif self.action == 'create':
            return CreatePostSerializer

    @action(methods=['PUT'], detail=True)
    def likes(self, request, *args, **kwargs):
        instance = self.get_object()
        user = request.user
        user_like = PostLikes.objects.filter(post=instance, user=user).first()
        if not user_like:
            PostLikes.objects.create(post=instance, user=user)
        return Response(status=200)

    @action(methods=['DELETE'], detail=True)
    def unlikes(self, request, *args, **kwargs):
        instance = self.get_object()
        user = request.user
        user_like = PostLikes.objects.filter(post=instance, user=user).first()
        if user_like:
            user_like.delete()
        return Response(status=200)


