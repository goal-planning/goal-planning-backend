from django.db import models
import uuid
from django.contrib.auth.models import User

# Create your models here.
class Activity(models.Model):
    class Meta:
        verbose_name_plural = 'activities'
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_name = models.CharField(max_length=300)
    category_options = (
        ('health','health'),
        ('general','general'),
        ('sales','sales'),
        ('project','project'),
        ('social','social'),
        ('retirement','retirement'),
        ('fulfillment','fulfillment'),
        ('other','other'),
    )
    category = models.CharField(
        choices=category_options,
        max_length=300,
        default=category_options[1]
    )
    priority_options = (
        ('low','low'),
        ('moderate','moderate'),
        ('high','high'),
    )
    priority = models.CharField(
        choices=priority_options,
        max_length=300,
        default=priority_options[0]
    )

    def __str__(self):
        return(f"{self.activity_name} | {self.category} | {self.priority}")
