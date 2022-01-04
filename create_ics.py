#!env python3

from icalendar import Calendar, Event, vCalAddress, vText
import pytz
from datetime import datetime
import os
from pathlib import Path

# Creating icalendar/event
event = Event()
event.add('summary', 'Python meeting about calendaring')
event.add('dtstart', datetime(2021, 1, 12, 8, 0, 0, tzinfo=pytz.utc))
event.add('dtend', datetime(2021, 1, 12, 10, 0, 0, tzinfo=pytz.utc))
event.add('dtstamp', datetime(2021, 1, 12, 0, 10, 0, tzinfo=pytz.utc))

# Adding Organizer
organizer = vCalAddress('MAILTO:organizer@example.com')
organizer.params['cn'] = vText('Organizer')
organizer.params['role'] = vText('CHAIR')
event['organizer'] = organizer

# Adding attendee
attendee = vCalAddress('MAILTO:foobar@example.com')
attendee.params['cn'] = vText('Foo Bar')
attendee.params['ROLE'] = vText('REQ-PARTICIPANT')
event.add('attendee', attendee, encode=0)

# Adding location
event['location'] = vText('Zoom Link')

# Adding events to calendar
cal = Calendar()
cal.add_component(event)

directory = str(Path(__file__).parent.parent) + "/"
# print(directory)
f = open(os.path.join(directory, 'example.ics'), 'wb')
f.write(cal.to_ical())
f.close()

# vim: ft=python
