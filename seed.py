from models import db,Todo

db.drop_all()
db.create_all()

todos = [
    Todo(title= "Study Bootcamp Codes"),
    Todo(title= "Prepare Breakfast"),
    Todo(title= "Wash Dishes", done=True),
    Todo(title= "Workout Today"),
    Todo(title= "Do Morning Skincare", done=True),
    Todo(title= "Check if Airline has Online Check-In")
]

db.session.add_all(todos)
db.session.commit()

