from unittest.util import _MAX_LENGTH
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
    ##
    #2 wasys to skin a cat here.
    #The above method will send the user to the 'post-detail'
    #of the newly created blog. (leveraging django's URL reverse magic)
    #contrarily, in users/views.py, after the new user registers, we validate the data,
    #give them a sucess message,
    #then redirect them to the homepage. 
    #
    #30 min mark on part 10
    # Corey talks about advantages and disadvantages of the 2 ways, but likes
    #the "class based views" that the django framework provides. cleaner, he says..
    #"funcion based views" are the alternative
    ##