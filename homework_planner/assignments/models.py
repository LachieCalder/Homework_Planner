from django.db import models

# Create your models here.

class Assignment(models.Model):
  due = models.DateField()
  subject = models.ForeignKey('Subject')
  description = models.CharField(max_length=200)
  done = models.BooleanField(default=False)

  def __unicode__(self):
	return self.description

class Subject(models.Model):
  name = models.CharField(max_length=30)

  def __unicode__(self):
	return self.name
