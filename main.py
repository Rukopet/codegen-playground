from fastapi import FastAPI, HTTPException, status
from ptx_schemas.models import UserCreate, UserResponse, ErrorResponse
import uvicorn

app = FastAPI(
    title="PTX API",
    description="API with OpenAPI generator integration",
    version="1.0.0",
    responses={
        400: {"model": ErrorResponse},
        401: {"model": ErrorResponse},
        403: {"model": ErrorResponse},
        404: {"model": ErrorResponse},
        500: {"model": ErrorResponse}
    }
)

@app.post(
    "/users",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
    responses={
        201: {"description": "User created successfully"},
        400: {"description": "Invalid input"},
        409: {"description": "User already exists"}
    }
)
async def create_user(user: UserCreate):
    # Demo implementation
    return UserResponse(
        id=1,
        username=user.username,
        email=user.email,
        role=user.role
    )

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000) 