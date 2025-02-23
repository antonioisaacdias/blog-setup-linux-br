from uuid import uuid4
from django.db import models

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False, null=False, blank=False, unique=True)
    title = models.CharField(max_length=100, null=False, blank=False)
    subject = models.CharField(max_length=100, null=False, blank=False)
    author = models.CharField(max_length=80, null=False, blank=False)
    content = models.TextField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)
    image = models.ImageField(upload_to='posts/', default='posts/Linux_logo.jpg')

    class Meta:
        db_table = 'posts'