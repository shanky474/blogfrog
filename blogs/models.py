from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=(('M', 'Male'),('F', 'Female')))
    profession = models.CharField(max_length=100)


class Blog(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    likes = models.IntegerField()
    dislikes = models.IntegerField()

    def increment_likes(self,likes):
        self.likes += 1
        return self.likes

    def increment_dislikes(self,dislikes):
        self.dislikes += 1
        return self.dislikes

