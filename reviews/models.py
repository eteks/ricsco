
from django.db import models

class Rating(models.Model):
  """
  A Meta Model to store Rating information.
  Ratings are used for Leads and Seller. They are stored in different tables to keep separated.
  """
  name = models.CharField(max_length=128)
  rating = models.FloatField(default=0.0)
  
  class Meta:
    abstract = True
    
  def __unicode__(self):
    return self.name

'''Reviews are different opinions such as grading and comments added by users'''    
class Review(models.Model):
  """
  A Meta Model to store Review information.
  Reviews are for Leads and Seller. User will enter their review abou the Leads and seller are stored in different tables.
  """
  actor = models.ForeignKey('actors.Actor', null=True)
  comments = models.CharField(max_length=512, blank=True)
  rating = models.PositiveSmallIntegerField(default=1)
  
  class Meta:
    abstract = True
    
  def __unicode__(self):
    return self.comments
