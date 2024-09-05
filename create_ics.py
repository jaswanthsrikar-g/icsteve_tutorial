
from ics import Calendar, Event
from datetime import datetime, timedelta

# Create a new calendar
cal = Calendar()

# Helper function to add events to the calendar
def add_event(name, start, duration_hours, days_of_week):
    for day in days_of_week:
        event = Event()
        event.name = name
        event.begin = start + timedelta(days=day)
        event.duration = timedelta(hours=duration_hours)
        cal.events.add(event)

# Define the start date (Monday of the current week)
start_date = datetime.now() - timedelta(days=datetime.now().weekday())

# Add events with their respective time slots
add_event("Wake Up & Meditation/Prayer", start_date.replace(hour=6, minute=0), 0.5, [0, 1, 2, 3, 4])
add_event("Gym Workout", start_date.replace(hour=6, minute=30), 2, [0, 1, 2, 3, 4])
add_event("Freshen Up", start_date.replace(hour=8, minute=30), 0.5, [0, 1, 2, 3, 4])
add_event("Breakfast", start_date.replace(hour=9, minute=0), 0.5, [0, 1, 2, 3, 4])
add_event("Focused Study/Work", start_date.replace(hour=9, minute=30), 3, [0, 1, 2, 3, 4])
add_event("Lunch Break", start_date.replace(hour=12, minute=30), 0.5, [0, 1, 2, 3, 4])
add_event("Piano Practice", start_date.replace(hour=13, minute=0), 2, [0, 2])
add_event("Guitar Practice", start_date.replace(hour=13, minute=0), 2, [1, 4])
add_event("Apply for Jobs/Internships", start_date.replace(hour=15, minute=0), 1, [0, 1, 2, 4])
add_event("Skill Building (Power BI, Python)", start_date.replace(hour=16, minute=0), 1, [0, 1, 2, 4])
add_event("Relaxation", start_date.replace(hour=17, minute=0), 1, [0, 2])
add_event("Socialize/Relax", start_date.replace(hour=17, minute=0), 1, [1, 4])
add_event("Dinner", start_date.replace(hour=18, minute=30), 1, [0, 1, 2, 3, 4])
add_event("Faith & Reflection", start_date.replace(hour=19, minute=30), 1, [1, 4])
add_event("Plan for Tomorrow/Unwind", start_date.replace(hour=20, minute=30), 1, [1, 3, 4])
add_event("Sleep", start_date.replace(hour=22, minute=30), 9, [0, 1, 2, 3, 4])

# Monday and Wednesday Classes (6:30 PM - 9:00 PM)
add_event("University Class", start_date.replace(hour=18, minute=30), 2.5, [0, 2])

# Thursday Class (2:00 PM - 5:00 PM)
add_event("University Class", start_date.replace(hour=14, minute=0), 3, [3])

# Save the calendar to a file
with open('jaswanth_daily_planner.ics', 'w') as my_file:
    my_file.writelines(cal)
