# coding: utf-8

from datetime import datetime

from flask import Flask
from flask import render_template

from views.todos import todos_view
from utils.logger import Logger

app = Flask(__name__)

# 动态路由
app.register_blueprint(todos_view, url_prefix='/todos')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/time')
def time():
    return str(datetime.now())

@app.route('/team')
def team():
    return str('Raindrop Studio')

@app.route('/wechat')
def wechat():
    Logger.println('echostr:'+request.args.get('echostr', ''))
    return request.args.get('echostr', '')