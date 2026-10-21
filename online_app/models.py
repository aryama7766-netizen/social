from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=250)
    image=models.ImageField(upload_to="post_images",null=True)
    description=models.CharField(max_length=300)
    created_at=models.DateTimeField(auto_now_add=True)
    owner=models.ForeignKey(User,on_delete=models.CASCADE,related_name="posts")


class Comment(models.Model):
    comment=models.CharField(max_length=300)
    added_at=models.DateTimeField(auto_now_add=True)
    owner=models.ForeignKey(User,on_delete=models.CASCADE,related_name="comments")
    post_object=models.ForeignKey(Post,on_delete=models.CASCADE,related_name="comments")


class Like(models.Model):
    post_obj=models.ForeignKey(Post,on_delete=models.CASCADE,related_name="likes")
    owner_obj=models.ForeignKey(User,on_delete=models.CASCADE,related_name="likes")
    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints=[
            models.UniqueConstraint(
                fields=["owner_obj","post_obj"],
                name="unique_user_post_like"
            )
        ]