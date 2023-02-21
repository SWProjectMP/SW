from typing import Dict, Union, List
from api.models import ProjectRoles, Tags, Faculty

def get_response_from_projects(project_to_response) -> Dict[str, Dict[str, Union[str, list]]]:
    projects = []
    for project in project_to_response:
        if project.is_active:
            projects.append({
                project.uniq_id : {
                    "label" : project.label,
                    "project_id" : project.uniq_id,
                    "profiles" : get_json_profiles(list(project.profiles.all()), project),
                    "description" : project.description,
                    "tags" : get_json_tags(list(project.tags.all())),
                    "pub_date" : str(project.pub_date),
                    "faculty" : project.faculty.display_name
                }
            })
    return projects

def get_json_profiles(profiles, project) -> List[Dict[str, list | str]]:
    profiles_s = []
    for profile in profiles:
        profiles_s.append({
            "username" : profile.username,
            "role" : profile.roles.all()[0].role if profile.roles.all() else "Участник",
            "project_role" : ProjectRoles.objects.filter(project_id=project.uniq_id, user_id=profile.profile_id)[0].role if ProjectRoles.objects.filter(project_id=project.uniq_id, user_id=profile.profile_id) else "Участник",
            "profile_id" : profile.profile_id
        })
    return profiles_s

def get_json_tags(tags):
    tags_s = []
    for tag in tags:
        if tag.is_visible:  
            tags_s.append(tag.display_tag)
    return tags_s

def get_tags(tags) -> list:
    tags_to_export = [
        x[0].tag for x in [
            Tags.objects.filter(display_tag=tag.strip()) for tag in tags
            ] if x
    ]
    return list(tags_to_export)