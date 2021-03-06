# coding: utf-8
import sys   
reload(sys)   
sys.setdefaultencoding('utf8')   

from datetime import datetime
import json, random, string
from flask import Flask, render_template, request, Response
import pingpp
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

@app.route('/pingpp')
def test_pingpp():
    return render_template('pingpp.html')

@app.route('/pay', methods=['POST'])
def do_charge():
    print request.url
    params = request.get_json()
    orderno = ''.join(random.sample(string.ascii_letters + string.digits, 8))

    if params['channel'] == 'alipay_wap ':
        extra = dict(
            success_url='http://www.yourdomain.com/success',
            cancel_url='http://www.yourdomain.com/cancel'
        )

    elif params['channel'] == 'upmp_wap':
        extra = dict(
            result_url='http://www.yourdomain.com/success?code='
        )

    elif params['channel'] == 'bfb_wap':
        extra = dict(
            result_url='http://www.yourdomain.com/result?code=',
            bfb_login=True
        )

    elif params['channel'] == 'wx_pub':
        extra = dict(
            open_id='your openid'
        )

    elif params['channel'] == 'wx_pub_qr':
        extra = dict(
            product_id='your productid'
        )

    elif params['channel'] == 'yeepay_wap':
        extra = dict(
            product_category ='1',
            identity_id='your identity_id',
            identity_type=1,
            terminal_type=1,
            terminal_id='your terminal_id',
            user_ua='your user_ua',
            result_url='http://www.yourdomain.com/result'
        )

    elif params['channel'] == 'jdpay_wap':
        extra = dict(
            success_url='http://www.yourdomain.com',
            fail_url='http://www.yourdomain.com',
            token='dsafadsfasdfadsjuyhfnhujkijunhaf'
        )
    else:
        extra = dict()



    if isinstance(params, dict):
        params['order_no'] = orderno
        params['app'] = dict(id='app_1Gqj58ynP0mHeX1q')
        params['currency'] = 'cny'
        params['client_ip'] = '127.0.0.1'
        params['subject'] = 'Your Subject'
        params['body'] = 'Your Body'
        params['extra'] = extra
    print params
    pingpp.api_key = 'sk_test_ibbTe5jLGCi5rzfH4OqPW9KC'
    response_charge = pingpp.Charge.create(api_key=pingpp.api_key, **params)
    print 'Response_Charge: ' + str(response_charge)
    return Response(json.dumps(response_charge), mimetype='application/json,charset=UTF-8')