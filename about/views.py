from django.shortcuts import render, get_object_or_404

from .models import About, Project, Skill

# Create your views here.


def about(request):

    about = About.objects

    return render(request, 'about/about.html', {'about': about.all()[0], 'projects': Project.objects.all(), 'skills': Skill.objects.all()})


def projectdetails(request, project_id):

    project = get_object_or_404(Project, pk=project_id)
    project_points = project.description.split(". ")

    return render(request, 'about/projectdetail.html', {'project': project, 'project_points': project_points})
