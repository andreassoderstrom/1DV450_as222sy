from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User

class Project(models.Model):
	name = models.CharField(max_length = 100)
	description = models.CharField(max_length = 100)
	start_date = models.DateField()
	end_date = models.DateField()
	owner_id = models.IntegerField()
	users = models.ManyToManyField(User, related_name='projects')

	def __unicode__(self):
		return self.name





class Status(models.Model):
	status_name = models.CharField(max_length=100)

	def __unicode__(self):
		return self.status_name



class Ticket(models.Model):
	name = models.CharField(max_length = 100)
	description = models.CharField(max_length = 100)

	project_id = models.ForeignKey(Project, related_name='tickets')
	status_id = models.ForeignKey(Status, related_name='tickets')
	user_id = models.ForeignKey(User, related_name='tickets')

	def __unicode__(self):
		return self.name


#forms ==========================
class ProjectForm(ModelForm):
	class Meta:
		model = Project
		exclude = ('owner_id')

class TicketForm(ModelForm):
	class Meta:
		model = Ticket
		exclude = ('project_id', 'user_id')
#================================