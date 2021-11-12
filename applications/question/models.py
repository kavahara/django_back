from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Question(models.Model):
    author = models.ForeignKey( User, on_delete=models.CASCADE,
                                related_name='question')
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name='question')
    title = models.TextField()
    image = models.ImageField(upload_to='')
    problem = models.TextField()
    public_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='answer')
    question = models.ForeignKey(Question, on_delete=models.CASCADE,
                                 related_name='answer')
    solution = models.TextField()
    public_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.question.title