import json
import uuid
from routes.routes import route

def handler(event, context):
    return route(event)

