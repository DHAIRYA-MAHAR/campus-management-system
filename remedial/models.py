from django.db import models

# Create your models here.
import uuid

class MakeUpClass(models.Model):
    subject = models.CharField(max_length=100)
    remedial_code = models.UUIDField(default=uuid.uuid4, editable=False)
