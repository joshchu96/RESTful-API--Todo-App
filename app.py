from flask import Flask, jsonify, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from models import db,Todo





app = Flask(__name__)


app.config['SECRET_KEY']='set'
app.config['SQLALCHEMY_DATABASE_URI']='postgresql:///todolist'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SQLCALCHEMY_ECHO']=True
debugger = DebugToolbarExtension(app)

db.init_app(app)
app.app_context().push()


@app.route('/')
def index():
    todos = Todo.query.all()
    return render_template("index.html", todos=todos)

@app.route('/api/todos')
def list_todos():
    all_todos = [todo.serialize() for todo in Todo.query.all()] #[{todo1 obj data}, {todo2 obj data}]
    return jsonify(todos = all_todos)

@app.route('/api/todos/<int:id>')
def get_todo(id):
    todo = Todo.query.get_or_404(id)
    return jsonify(todo=todo.serialize())

@app.route('/api/todos', methods=['POST'])
def create_todo():
    new_todo = Todo(title=request.json["title"])
    db.session.commit()
    response_json = jsonify(todo= new_todo.serialize())
    return (response_json, 201)

@app.route('/api/todos/<int:id>', methods=["PATCH"])
def update_todo(id):
    todo = Todo.query.get_or_404(id)
    todo.title = request.json.get('title', todo.title)
    todo.done = request.json.get('done', todo.done)
    db.session.commit()
    return jsonify(todo=todo.serialize())

@app.route('/api/todos/<int:id>', methods=["DELETE"])
def delete_todo(id):
    todo = Todo.query.get_or_404(id)
    db.session.delete(todo)
    db.session.commit()
    return jsonify(message="deleted")
