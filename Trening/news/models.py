from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    STATUSES = (('draft', 'Roboczy'), ('published', 'Opublikowany'))
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique_for_date='published')
    author = models.ForeignKey(User, related_name='news_posts',
                               on_delete=models.CASCADE)
    content = models.TextField()

    published = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    status = models.CharField(max_length=10, choices=STATUSES,
                              default='draft')

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.published.year,
                                           self.published.month,
                                           self.published.day,
                                           self.slug])

    class Meta:
        ordering = ('published',)

    def __str__(self): return self.title


class Comment(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    post = models.ForeignKey(Post, related_name='comments',
                             on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return f'Komentarz dodany przez {self.name} dla posta' \
               f'{self.post}'
