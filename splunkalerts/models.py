from django.db import models
from django.utils import timezone

class WebhookTransaction(models.Model):
    UNPROCESSED = 1
    PROCESSED = 2
    ERROR = 3

    STATUSES = (
        (UNPROCESSED, 'Unprocessed'),
        (PROCESSED, 'Processed'),
        (ERROR, 'Error'),
    )
    date_event_generated = models.DateTimeField()
    date_received = models.DateTimeField(default=timezone.now)
    body = models.TextField()
    request_meta = models.TextField()
    status = models.CharField(max_length=250, choices=STATUSES, default=UNPROCESSED)

    def __unicode__(self):
        return self.date_event_generated

TransactionalData = ''
class Message(models.Model):
    date_processed = models.DateTimeField(default=timezone.now)
    webhook_transaction = models.OneToOneField(WebhookTransaction, on_delete=models.DO_NOTHING)
    search_name = models.CharField(max_length=250)
    host = models.CharField(max_length=250)
    
    def __str__(self):
        return self.search_name