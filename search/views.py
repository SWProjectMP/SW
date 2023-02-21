from django.shortcuts import render
from api.models import Faculty,Tags,Project,ProjectImages
from api.projects import get_response_from_projects, get_tags

class PProject:
    def __init__(self, project, tags):
        self.label = project.label
        self.uniq_id = project.uniq_id
        self.description = project.description
        self.tags = tags
        self.image = ProjectImages.objects.filter(project=self.uniq_id)
        self.image = self.image[0].image if self.image else "static/img/search__Page/head.svg"
        print(self.image)

# Create your views here.
def index(request):
    facultis_all = list(Faculty.objects.all())
    facultis1 = facultis_all[:5]
    facultis2 = facultis_all[5:]

    tags_all = list(Tags.objects.all())
    tags1 = tags_all[:7]
    tags2 = tags_all[7:]

    if request.GET:

        request.GET = dict(request.GET)
        print(request.GET)
        facult = request.GET['faculty'][0]
        faculty = Faculty.objects.filter(name=facult)[0].id
        # last_project = request.GET['last_id'][0]
        tags = request.GET['tags'][0].replace('"', '').split(",")
        # last_project = Project.objects.filter(uniq_id=last_project)
        if len(tags[0]):
            tags = get_tags(tags)
        else:
            tags = [x for x in list(Tags.objects.all())]
        
        

        project_to_response = Project.objects.filter(
            faculty=faculty,
            tags__in=tags
            )
        project_to_response = project_to_response[:15]
        prf = []
        for project in project_to_response:
            prf.append(
                PProject(project,[tag for tag in project.tags.all()])
            )
        return render(request, 'search/searchPage.html', {"facultis1": facultis1, "facultis2" : facultis2,
                                                        "tags" : tags, "projects": prf})
    
    projects = list(Project.objects.all())[:15]
    prf = []
    for project in projects:
        prf.append(
            PProject(project,[tag for tag in project.tags.all()])
        )
    print(projects[0].tags.all())
    return render(request, 
                    'search/searchPage.html', 
                    {"facultis1": facultis1, "facultis2" : facultis2,
                     "facults_all" : facultis_all,"tags" : tags_all, "projects": prf})
