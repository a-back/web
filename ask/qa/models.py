from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    likes = models.ManyToManyField(User, related_name='likes')

    def __unicode__(self):
        return self.title
    
    def get_url(self):
	return reverse('question', kwargs={'pk': self.id})
        #return '/question/' + str(question.id) + '/'

#    class Meta:
#        ordering = ['added_at']
# add create
# https://docs.djangoproject.com/en/1.9/ref/models/instances/



class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __unicode__(self):
        return self.title

    def get_url(self):
	return '/question/' + str(self.question.id) + '/'


#    class Meta:
#        ordering = ['added_at']

