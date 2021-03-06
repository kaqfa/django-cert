from django.db import models
from django.utils import timezone
# Create your models here.


class TimeStamped(models.Model):
    created_at = models.DateTimeField(editable=False, default=timezone.now())
    updated_at = models.DateTimeField(editable=False, default=timezone.now())

    def save(self, *args, **kwargs):
        # if not self.created_at:
        #     self.created_at = timezone.now()

        self.updated_at = timezone.now()
        return super(TimeStamped, self).save(*args, **kwargs)

    class Meta:
        abstract = True