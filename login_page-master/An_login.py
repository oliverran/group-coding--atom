# -*- coding: utf-8 -*-
from flask import Flask, render_template
from flask_script import Manager
from flask_bootstrap import Bootstrap

app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)

app.config['SECRET_KEY'] = 'hard to guess string'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://<username>:<password>@<server_address>/<db_name>'


if __name__ == '__main__':
    # app.run()
    # db.create_all()
    manager.run()
