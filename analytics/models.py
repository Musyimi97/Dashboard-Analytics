from django.db import models
from django.conf import settings
from django.contrib.contenttypes import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
User=settings.AUTH_USER_MODEL

class ObjectViewed(models.Model):
    # user instance
    user=models.ForeignKey(blank=True, null=True),
    # user,product, address, location  
    content_type= models.ForeignKey(ContentType)
    # user id, product id,address id
    object_id =models.PositiveIntegerField() 
    # object instance
    content_object= GenericForeignKey('content_type', 'object_id')
    timestamp=models.DateTimeField(auto_now_add=True)
    ip_address=models.CharField(max_length=220, blank=True,null=True)

    def __str__(self):
        return "%s viewed %s" %(self.content_object,self.timestamp)

    class Meta:
        ordering=['-timestamp']
        verbose_name = 'Object Viewed'
        verbose_name_plural = 'Objects Viewed'
    
