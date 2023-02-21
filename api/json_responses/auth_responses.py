from api.json_responses.base_response import BaseResponse

class AuthResponse(BaseResponse):
    userAuthenticated = {
                "status" : "error",
                "error" : "Already authenticated"
            }
    class EmailVerify:
        profileNotExistResponse = {
            "is_success" : False,
            "status": "Profile doesn't exists"
        }
        profileVerifyiedResponse = {
            "is_succes": True,
            "status": "Already verifyied"
            }
        authKeyErrorResponse = {
            "is_success": False,
            "status": "Authentication key auth failed"
        }
        verifySuccessResponse = {
            "is_success": True,
            "status": "Verification succesful"
        }
    class Register:
        profileExists = {
                "status" : "error",
                "error" : "User already exists"
            }
    class Login:
        incorrectData = {
                    "status": "error",
                    "error": "Incorrect password or username"
                }
        