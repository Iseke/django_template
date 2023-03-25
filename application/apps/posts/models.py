from django.db import models


class Post(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Название"
    )
    text = models.TextField(verbose_name="Описание")
    created_by = models.ForeignKey(
        to='users.User',
        on_delete=models.CASCADE,
        verbose_name='Кем создано',
        related_name='post'
    )
    created_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )
    updated_date = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата обновления"
    )
    deleted_date = models.DateTimeField(
        verbose_name="Дата удаления",
        null=True, blank=True
    )

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        ordering = ["-created_date"]

    def __str__(self):
        return f'{self.title} - {self.created_by}'


class PostLikes(models.Model):
    post = models.ForeignKey(
        to='posts.Post',
        on_delete=models.CASCADE,
        related_name='post_likes'
    )
    user = models.ForeignKey(
        to='users.User',
        on_delete=models.CASCADE,
        related_name='post_likes'
    )
    created_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )

    class Meta:
        ordering = ["-created_date"]
        unique_together = ('post', 'user',)

