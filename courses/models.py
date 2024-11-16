from django.conf import settings
from django.db import models



class Course(models.Model):
    name = models.CharField(max_length=100, default="Unnamed Course")
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)  # Default price

    start_date = models.DateField()
    title = models.CharField(max_length=255)
    description = models.TextField()
    instructor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='courses')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    duration = models.CharField(max_length=100)
    video = models.FileField(upload_to='course_videos/', blank=True, null=True)
    level = models.CharField(
        max_length=50, 
        choices=[('beginner', 'Beginner'), 
                 ('intermediate', 'Intermediate'), 
                 ('advance', 'Advanced')]
    )

    def __str__(self):
        return self.title
