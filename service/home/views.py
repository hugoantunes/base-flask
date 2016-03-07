from flask import Blueprint

home = Blueprint(
    'home',
    __name__,
    template_folder='templates',
    static_folder='static'
)


@home.route('/')
def login():
    return "ok"
