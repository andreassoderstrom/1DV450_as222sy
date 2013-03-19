# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseServerError
from django.shortcuts import get_list_or_404, render, get_object_or_404, redirect
from projectmanager.models import Project, ProjectForm , Ticket, TicketForm, Status, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required

#project List
@login_required(login_url='/login')
def project_list(request, project_id = None):
	if request.method == "POST":
		projects = Project.objects.filter(name__contains = request.POST["search"])
		return render(request, 'projects/list.html', {"projects" : projects})
	else:
		if project_id:
			project = get_object_or_404(Project.objects.filter(id = project_id))
			if project.is_member(request.user.id):
				tickets = Ticket.objects.filter(project_id_id = project_id)
				return render(request, 'projects/project.html', {"project" : project, "tickets" : tickets})
			else:
				return HttpResponse("You do not have permission")
		else:
			projects = get_list_or_404(Project.objects.order_by('name'))
			return render(request, 'projects/list.html', {"projects" : projects})

#project Add
@login_required(login_url='/login')
def project_add(request):
	if request.method == "POST":
		form = ProjectForm(request.user.id, request.POST)
		if form.is_valid():
			form.instance.owner_id = request.user.id
			form.save()
			form.instance.users.add(request.user)
			return redirect(project_list)
	else:
		form = ProjectForm(request.user.id)

	return render(request, 'projects/add.html', {"form": form})

#project Delete
@login_required(login_url='/login')
def project_delete(request, project_id= None):
	project = get_object_or_404(Project, pk=project_id)
	if project.owned_by(request.user.id):
		project.delete()
		return redirect(project_list)
	else:
		return HttpResponse('You are not the owner')

#project Edit
@login_required(login_url='/login')
def project_edit(request, project_id= None):
	project = get_object_or_404(Project, pk=project_id)	
	if project.owned_by(request.user.id):
		if request.method == "POST":
			form = ProjectForm(request.user.id, request.POST, instance = project)
			if form.is_valid():
				try:
					form.save()
					form.instance.users.add(request.user)
					return redirect('project_list')
				except:
					return HttpResponseServerError()
		else:
			form = ProjectForm(request.user.id, instance = project)
	else:
		return HttpResponse("You do not have permission")
	return render(request, 'projects/edit.html', {"form" : form})

#Ticket view
@login_required(login_url='/login')
def ticket(request, project_id, ticket_id = None):
	project = get_object_or_404(Project.objects.filter(id = project_id))
	if project.is_member(request.user.id):
		ticket = get_object_or_404(Ticket.objects.filter(id = ticket_id))
		status = get_object_or_404(Status.objects.filter(tickets = ticket_id))
		return render(request, 'tickets/ticket.html', {"ticket" : ticket, "status": status})
	else:
		return HttpResponse("You do not have permission")


#ticket add
@login_required(login_url='/login')
def ticket_add(request, project_id = None):
	project = get_object_or_404(Project, pk = project_id)
	if project.is_member(request.user.id):
	
		if request.method == "POST":
			form = TicketForm(request.POST)
			if form.is_valid():
				form.instance.user_id_id = request.user.id
				form.instance.project_id_id = project_id
				form.save()
				return HttpResponseRedirect('/projects/%i/' % int(project_id))
		else:
			form = TicketForm()
	else:
		return HttpResponse("You do not have permission")

	return render(request, 'tickets/add.html', {"form": form, "project" : project})

#tcket Edit
@login_required(login_url='/login')
def ticket_edit(request, project_id = None, ticket_id = None):
	ticket = get_object_or_404(Ticket, id = ticket_id)
	project = get_object_or_404(Project, pk = project_id)
	currentUser = request.user

	if ticket.owned_by(currentUser.id) or project.owned_by(currentUser.id):
		if request.method == "POST":
			form = TicketForm(request.POST , instance = ticket)
			if form.is_valid():
				try:
					form.save()
					return HttpResponseRedirect("/projects/" + project_id + "/ticket/" + ticket_id)
				except:
					return HttpResponseServerError()
		else:
			form = TicketForm(instance = ticket)
	else:
		return HttpResponse("You do not have permission")
	return render(request, "tickets/edit.html", {"form": form, "ticket": ticket, "currentUser": currentUser})


#ticket Delete
@login_required(login_url='/login')
def ticket_delete(request, project_id= None, ticket_id = None):
	ticket = get_object_or_404(Ticket, id = ticket_id)
	project = get_object_or_404(Project, pk = project_id)
	currentUser = request.user

	if ticket.owned_by(currentUser.id) or project.owned_by(currentUser.id):
		ticket.delete()
		return HttpResponseRedirect('/projects/%i/' % int(project_id))
	else:
		return HttpResponse("You dont have permission yo")



#log in
def login_user(request):
	message = ''
	if request.method == "POST":
		form = LoginForm(request.POST)
		if form.is_valid():
			username_to_try = form.cleaned_data["username"]
			password_to_try = form.cleaned_data["password"]

			user = authenticate(username=username_to_try, password=password_to_try)
			if user is not None:
				if user.is_active:
					login(request, user)
					request.session['has_logged_in'] = True
					return redirect('project_list')
				else:
					return HttpResponse("<p> Your account is disabled!! </p>")
			else:
				message = "Wrong username or password"
	else:
		form = LoginForm()

	return render(request, 'login.html', {'form' : form, 'message' : message})


def logout_user(request):
	logout(request)
	return redirect('login')

