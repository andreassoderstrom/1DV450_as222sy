from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms

class Project(models.Model):
	name = models.CharField(max_length = 100)
	description = models.CharField(max_length = 100)
	start_date = models.DateField()
	end_date = models.DateField()
	owner_id = models.IntegerField()
	users = models.ManyToManyField(User, related_name='projects')

	def __unicode__(self):
		return self.name


	def owned_by(self, user):
		return self.owner_id == user

	def is_member(self, user):
		return self.users.filter(pk = user)




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

	def owned_by(self, user):
		return self.user_id == user 


#forms ==========================
class ProjectForm(ModelForm):
	def __init__(self, user_id, *args, **kwargs):
		super(ProjectForm, self).__init__(*args, **kwargs)
		self.fields['users'].queryset = \
		User.objects.exclude(id = user_id)
	class Meta:
		model = Project
		exclude = ('owner_id')

class TicketForm(ModelForm):
	class Meta:
		model = Ticket
		exclude = ('project_id', 'user_id')


#login
class LoginForm(forms.Form):
	username = forms.CharField(max_length=20)
	password = forms.CharField(widget = forms.PasswordInput)
#================================
