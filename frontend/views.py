from django.shortcuts import render

from api.models import Project, ProjectImages


class PProject:
    def __init__(self, project, tags):
        self.label = project.label
        self.uniq_id = project.uniq_id
        self.description = project.description
        self.tags = tags
        self.images = ProjectImages.objects.filter(project=self.uniq_id)
        if not self.images:
            self.image = "static/img/search__Page/head.svg"
        else:
            self.image = self.images[0].image


def home_view(request):
    return render(request, 'frontend/mainPage.html', {"user" : request.user.is_authenticated})

def project_view(request):
    return render(request, 'frontend/projects.html')

def project(request, project_id):

    project = Project.objects.filter(uniq_id=project_id)[0]
    project = PProject(project,[tag for tag in project.tags.all()][:4])

    return render(request, 'frontend/project_page.html', {"project": project})