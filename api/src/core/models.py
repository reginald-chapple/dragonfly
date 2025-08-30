from django.db import models
from django.utils import timezone
from django.utils.timezone import now

class BaseModel(models.Model):
    created_at = models.DateTimeField(default=now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        
    def save(self, *args, **kwargs):
        if not self.id:  # Check if the object is being created (no ID yet)
            self.updated_at = timezone.now()  # Set initial updated_at on creation
        super().save(*args, **kwargs) 