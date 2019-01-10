from django.db import models
# Importing User Information as Foreign key.
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length = 100)  # Max length in this filed can only be 100.
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)  # To the date field the date will b automatically added.
    thumbnail = models.ImageField(blank=True)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=None)
    # Fields in this model will map to the colum ns of the database.
    # Models created here should be then migrated(connection to the database should be established).
    def __str__(self):
        return self.title
        # In order of printing the class name, it names the object with its title.

# Only displaying few part of the body.
    def short(self):
        if len(self.body) <= 50:
            return self.body
        else:
            a = self.body.split(' ')
            st = ''
            l = 0
            while l < 50:
                l = l + len(a[0])
                st = st + a[0] + ' '
                a.remove(a[0])
            else:
                return st + '....'
