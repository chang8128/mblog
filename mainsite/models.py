from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length=200)
	slug = models.CharField(max_length=200)
	body = models.TextField()
	pub_date = models.DateTimeField(default=timezone.now)
	
	class Meta:
	    ordering = ('-pub_date',)
	    
	def __unicode__(self):
		return self.title
		

class Stock0(models.Model):
    ai_date = models.DateField()
    stockname = models.CharField(max_length=30)
    code = models.CharField(max_length=30)
    industry = models.CharField(max_length=30)
    percent = models.DecimalField(max_digits=10, decimal_places=2)
    buyprice = models.DecimalField(max_digits=10, decimal_places=2)
    pub_date = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ('-ai_date',)
        
    def __unicode__(self):
        return self.ai_date     