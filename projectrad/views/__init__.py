from projectrad.views.loja import loja
from projectrad.views.admin import admin
from projectrad.views.produtos import produtos
from projectrad.views.usuario import usuario

from flask import Blueprint
from flask import render_template

views = Blueprint("views", __name__, 'static', '/a', 'templates')
views.register_blueprint(loja)
views.register_blueprint(admin)
views.register_blueprint(produtos)
views.register_blueprint(usuario)


@views.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@views.route('/replace', methods=["GET"])
def replace():
    return render_template("replacer.html")