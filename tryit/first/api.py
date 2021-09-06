from ninja import NinjaAPI, Schema
from asgiref.sync import sync_to_async
from typing import List
from first.models import Event
from pydantic import BaseModel as PydanticBaseModel

api = NinjaAPI()


class BaseModel(PydanticBaseModel):
    class Config:
        arbitrary_types_allowed = True

class EventSchema(BaseModel, Schema):
    id: int
    name: str
    is_active: bool

@api.get("/hello")
def hello(request):
    return "Hello world"

@api.get("/events", response=List[EventSchema])
async def events(request):
    events = await sync_to_async(list)(Event.objects.all())
    return events
