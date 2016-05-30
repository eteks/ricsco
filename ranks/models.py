from django.db import models

from django.db import models

class Ranking(models.Model):
  """
  A Meta Model to store Ranking information.
  Rankings are used for Leads and Seller. They are stored in different tables to keep separated.
  """
  rank = models.FloatField(default=0.0)
  
  class Meta:
    abstract = True
    
  def __unicode__(self):
    return str(self.rank)

