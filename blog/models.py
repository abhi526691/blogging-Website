from django.db import models
from django.contrib.auth.models import User

# Create your models here.
status = (
    (0, 'DRAFT'),
    (1, 'ACTIVE')
)

category = (
    ('travel', 'Travel'),
    ('food', 'Food'),
    ('news', 'News'),
    ('technology', 'Technology'),
    ('lifestyle', 'Lifestyle'),
    ('fashion', 'Fashion'),
    ('personal', 'Personal')


)

class blog(models.Model):
    title = models.CharField(max_length=50, unique=True)
    content = models.TextField()
    updated_on = models.DateField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=50, unique=True)
    created_on = models.DateField(auto_created=True, auto_now=True)
    status = models.IntegerField(choices=status, default=0)
    category = models.CharField(choices = category, max_length=50, null=True, blank=True)
    img = models.ImageField(upload_to = 'images/', null=True, blank = True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return self.title



