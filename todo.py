from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow() # Flask-Marshmallowの利用設定

def init_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db/todoitems.db"
    db.init_app(app)


def init_schema(app): # Flask-Marshmallowオブジェクトをappで初期化
    ma.init_app(app)

class ToDoItem(db.Model):
    __tablename__ = "todoitems"
    item_id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable = False, default = False)
    done = db.Column(db.Boolean, nullable = False)


class ItemSchema(mb.schema):
    class Meta:
        fields = ("item_id", "title", "done")


# class ToDoList:

#     def add(self, title):
#         item = ToDoItem(title = title, done = False)
#         db.session.add(item)
#         db.session.commit()


#     def delete(self, item_id):
#         item = ToDoItem.query.filter_by(item_id = item_id).first()
#         db.session.delete(item)
#         db.session.commit()



#     def get_all(self):
#         items = ToDoItem.query.all()
#         return items


#     def delete_doneitem(self):
#         ToDoItem.query.filter_by(done = True).delete()
#         db.session.commit()

    
#     def update_done(self, items):
#         for item in self.get_all():
#             if item.item_id in items:
#                 item.done = True
#             else:
#                 item.done = False
#         db.session.commit()