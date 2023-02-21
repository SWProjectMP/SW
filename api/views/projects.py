from django.http import JsonResponse
from django.core.handlers.wsgi import WSGIRequest

from api.models import Project, Tags, Faculty
from api.json_responses import ProjectResponse
from api.settings import *

from api.projects import get_response_from_projects, get_tags


def get_projects(request: WSGIRequest) -> JsonResponse:
    if request.method != "POST":
        return JsonResponse({"data": ProjectResponse.methodError})

    if "faculty" not in request.POST or "tags" not in request.POST or "last_id" not in request.POST:
        return JsonResponse({"data": ProjectResponse.invalidArgs})

    last_project = Project.objects.filter(uniq_id=request.POST["last_id"])
    if not last_project:
        return JsonResponse({"data": ProjectResponse.lastProjectNotExists})

    tags = get_tags(request.POST['tags'].replace('"', '').split(","))
    faculty = Faculty.objects.filter(name=request.POST['faculty'])[0].id
    
    project_to_response = Project.objects.filter(
        id__gt=last_project[0].id,
        faculty=faculty,
        tags__in=tags
        )
    project_to_response = project_to_response[:PROJECTS_TO_RESPONSE]

    if len(project_to_response) <= PROJECTS_TO_RESPONSE:
        return JsonResponse({
            "status": "200",
            "projects" : get_response_from_projects(project_to_response),
            "last_id": None
        })
                