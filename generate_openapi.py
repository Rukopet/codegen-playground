from fastapi.openapi.utils import get_openapi
from main import app
import json

def generate_openapi_spec():
    openapi_schema = get_openapi(
        title=app.title,
        version=app.version,
        description=app.description,
        routes=app.routes,
    )
    
    # Write OpenAPI spec to file
    with open("openapi.json", "w") as f:
        json.dump(openapi_schema, f, indent=2)

if __name__ == "__main__":
    generate_openapi_spec() 