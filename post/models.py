from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()

LIKE_CHOICES = (
    ('like', 'like'),
    ('dislike', 'dislike')
)


class Post(models.Model):
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE)
    posted_time = models.DateTimeField(auto_now=True)
    article = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return self.article


class Like(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE)
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name='likes')
    value = models.CharField(max_length=10, choices=LIKE_CHOICES)


class Comment(models.Model):
    article = models.ForeignKey(Post,
                                on_delete=models.CASCADE)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE)
    text = models.TextField()


class CommentLike(models.Model):
    comment = models.ForeignKey(Comment,
                                on_delete=models.CASCADE)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE)
    value = models.CharField(max_length=10, choices=LIKE_CHOICES)

