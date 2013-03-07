# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseServerError
from django.shortcuts import get_list_or_404, render, get_object_or_404, redirect
from projectmanager.models import Project, ProjectForm , Ticket, TicketForm, Status


def project_list(request, project_id = None):

	if project_id:
		project = get_object_or_404(Project.objects.filter(id = project_id))
		tickets = Ticket.objects.filter(project_id_id = project_id)
		return render(request, 'projects/project.html', {"project" : project, "tickets" : tickets})
	else:
		projects = get_list_or_404(Project.objects.order_by('name'))
		return render(request, 'projects/list.html', {"projects" : projects})

def project_add(request):
	if request.method == "POST":
		form = ProjectForm(request.POST)
		if form.is_valid():
			form.instance.owner_id = 1
			form.save()
			return redirect(project_list)
	else:
		form = ProjectForm()

	return render(request, 'projects/add.html', {"form": form})



def ticket(request, project_id, ticket_id = None):
	ticket = get_object_or_404(Ticket.objects.filter(id = ticket_id))
	status = get_object_or_404(Status.objects.filter(tickets = ticket_id))
	return render(request, 'tickets/ticket.html', {"ticket" : ticket, "status": status})


def ticket_add(request, project_id = None):
	project = get_object_or_404(Project, pk = project_id)
	if request.method == "POST":
		form = TicketForm(request.POST)
		if form.is_valid():
			form.instance.user_id_id = 1
			form.instance.project_id_id = project_id
			form.save()
			return HttpResponseRedirect('/projects/%i/' % int(project_id))
	else:
		form = TicketForm()

	return render(request, 'tickets/add.html', {"form": form, "project" : project})





