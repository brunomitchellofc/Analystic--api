import os
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
 
from api.db.session import get_session

from.models import (
  EventModel,
  EventListSchema,
  EventCreateSchema,
  EventUpdateSchema
)

router = APIRouter()

# Get Data Here
# List view
#GET /api/events/
@router.get("/", response_model=EventListSchema)
def read_events(session: Session = Depends(get_session)):
  # a bunch of items in a table
  query = select(EventModel).order_by(EventModel.id.desc()).limit(10)
  results = session.exec(query).all()
  return {
    "results": results,
    "count": len(results)
  }

# SEND DATA HERE
# POST /API/EVENTS
# Create View
@router.post("/", response_model=EventModel)
def create_event(
   payload:EventCreateSchema, 
   session: Session = Depends(get_session)):
  # a bunch of items in a table
  data = payload.model_dump() # payload -> dict -> pydantic
  obj = EventModel.model_validate(data)
  session.add(obj)
  session.commit()
  session.refresh(obj)

  return obj



#GET /api/events/12
@router.get("/{event_id}", response_model=EventModel)
def get_event(event_id:int, session: Session = Depends(get_session)):
  # a single row
    query = select(EventModel).where(EventModel.id == event_id)
    result = session.exec(query).first()
    if not result:
       raise HTTPException(status_code=404, detail="Event not found")
    return result


#Updata the data
#PUT /api/events/12
@router.put("/{event_id}", response_model=EventModel)
def update_event(event_id:int, 
                 payload:EventUpdateSchema, 
                 session: Session = Depends(get_session) ) -> EventModel:
  # a single row
  query = select(EventModel).where(EventModel.id == event_id)
  obj = session.exec(query).first()
  if not obj:
      raise HTTPException(status_code=404, detail="Event not found")
  
  data = payload.model_dump()
  for k, v in data.items():
     setattr(obj, k, v)

  session.add(obj)
  session.commit()
  session.refresh(obj)
  return obj
