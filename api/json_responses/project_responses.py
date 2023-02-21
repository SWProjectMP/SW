from api.json_responses.base_response import BaseResponse

class ProjectResponse(BaseResponse):
    noMoreProjects = {
                    "last_id": None,
                    "status": "error",
                    "error" : "No more projects",
                }
    lastProjectNotExists = {
        "status": "error",
        "error" : "Last project doesn't exists"
    }