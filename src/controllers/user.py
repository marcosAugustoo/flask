from flask import Blueprint, request
from src.app import User, db
from http import HTTPStatus

# padrão restful (plural)
app = Blueprint('user', __name__, url_prefix='/users')


def _creat_app():
    data = request.json
    user = User(username=data['username'])
    db.session.add(user)
    db.session.commit()


@app.route('/', methods=['GET', 'POST'])
def handle_user():
    if request.method == 'POST':
        return {'message': 'User created!'}, HTTPStatus.CREATED
    else:
        return {'users': []}
