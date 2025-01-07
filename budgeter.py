from datetime import datetime, timedelta
from error import *

class Event:
    activity: object
    date: datetime

    def __init__(self, activity: object, date: datetime):
        self.activity = activity
        self.date = date
    
    def __lt__(self, o: object) -> bool:
        if not isinstance(o, Event):
            raise TypeError
        return self.date < o.date
    
    def __eq__(self, o: object) -> bool:
        if not isinstance(o, Event):
            raise TypeError
        return self.date == o.date
    
    def __str__(self) -> str:
        return f"{self.activity} on {pretty_datetime(self.date)}"
    
    def __repr__(self) -> str:
        return str(self)


class EventList:
    events: list[Event]
    
    def __init__(self):
        self.events = []
    
    def __iter__(self):
        return iter(self.events)
    
    def __getitem__(self, index: int) -> Event:
        return self.events[index]
    
    def __len__(self) -> int:
        return len(self.events)
    
    def add(self, event: Event) -> bool:
        for i in range(len(self.events)):
            if self.events[i] < event or self.events[i] == event:
                self.events.insert(i, event)
                return True
        self.events.append(event)
        return False
    
    def pop(self, index: int) -> Event:
        return self.events.pop(index)
    

class Todo(EventList):
    pass

class Category:
    name: str
    todo: Todo

def pretty_datetime(dt: datetime) -> str:
    months = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
    # weekdays = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    retval: str = f"{dt.day} {months[dt.month-1][:3]} {dt.year%100}"
    if dt.hour + dt.minute + dt.second > 0:
        retval += f" at {dt.hour}{dt.minute}"
    return retval

def main():
    pass