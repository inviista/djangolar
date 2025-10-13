from django.utils import timezone

from django.db import models


class AbstractSoftDeletableModel(models.Model):
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()

    class Meta:
        abstract = True


