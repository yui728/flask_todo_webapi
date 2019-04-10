from flask import Flask, jsonify, request
from todo import ToDoItem, init_db, init_schema
from todo import item_schema, items_schema


app = Flask(__name__)

db = init_db(app)
init_schema(app)
# todolist = ToDoList()

# 全てのToDoを取得する
@app.route("/api/todoitems", methods = ["GET"])
def get_todoitems():
    items = ToDoItem.query.all()
    return items_schema.jsonify(items)


#  item_idで指定したToDoを取得する
@app.route("/api/todoitems/<int:item_id>", methods = ["GET"])
def get_todoitem(item_id):
    item = ToDoItem.query.filter_by(item_id = item_id).first_or_404()
    return item_schema.jsonify(item)


# 新しいToDoを追加する
@app.route("/api/todoitems", methods = ["POST"])
def add_todoitem():
    if not "title" in request.json:
        return "error"
    item = ToDoItem(title = request.json["title"], done = False)
    db.session.add(item)
    db.session.commit()
    return item_schema.jsonify(item)


# 指定したitem_idのToDoを削除する
@app.route("/api/todoitems/<int:item_id>", methods = ["DELETE"])
def delete_todoitem(item_id):
    item = ToDoItem.query.filter_by(item_id = item_id).first_or_404()
    db.session.delete(item)
    db.session.commit()
    return jsonify({"result": True})


# 指定したitem_idのToDoのdoneを更新する
@app.route("/api/todoitems/<int:item_id>", methods = ["PUT"])
def update_todoitem(item_id):
    item = ToDoItem.query.filter_by(item_id = item_id).first_or_404()
    item.done = not item.done
    db.session.commit()
    return item_schema.jsonify(item)
