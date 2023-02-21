class BaseResponse:
    success = {
                "status" : "OK"
            }
    methodError = {
            "status" : "error",
            "error" : "Please, use the POST method"
        }
    invalidArgs = {
                    "status": "error",
                    "error": "Invalid args"
                }
    request_error = {
        "status": "error",
        "error" : "Request error are accured"
    }