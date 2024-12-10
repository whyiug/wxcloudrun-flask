from datetime import datetime
from flask import render_template, request
from run import app
from wxcloudrun.dao import delete_counterbyid, query_counterbyid, insert_counter, update_counterbyid
from wxcloudrun.model import Counters
from wxcloudrun.response import make_succ_empty_response, make_succ_response, make_err_response
import logging

logger = logging.getLogger('log')

@app.route('/')
def index():
    """
    :return: 返回index页面
    """
    return render_template('index.html')


@app.route('/api/count', methods=['POST'])
def count():
    """
    :return:计数结果/清除结果
    """

    # 获取请求体参数
    params = request.get_json()

    # 检查action参数
    if 'action' not in params:
        return make_err_response('缺少action参数')

    # 按照不同的action的值，进行不同的操作
    action = params['action']

    # 执行自增操作
    if action == 'inc':
        counter = query_counterbyid(1)
        if counter is None:
            counter = Counters()
            counter.id = 1
            counter.count = 1
            counter.created_at = datetime.now()
            counter.updated_at = datetime.now()
            insert_counter(counter)
        else:
            counter.id = 1
            counter.count += 1
            counter.updated_at = datetime.now()
            update_counterbyid(counter)
        return make_succ_response(counter.count)

    # 执行清0操作
    elif action == 'clear':
        delete_counterbyid(1)
        return make_succ_empty_response()

    # action参数错误
    else:
        return make_err_response('action参数错误')


@app.route('/api/count', methods=['GET'])
def get_count():
    """
    :return: 计数的值
    """
    counter = Counters.query.filter(Counters.id == 1).first()
    return make_succ_response(0) if counter is None else make_succ_response(counter.count)


@app.route('/api/message', methods=['POST'])
def receive_message():
    """
    :return: 接收并打印用户消息
    """
    # 获取请求体参数
    params = request.get_json()
    logger.info("我在这里呀")

    # 检查message参数
    if 'message' not in params:
        return make_err_response('缺少message参数')

    # 打印消息
    message = params['message']
    print(f"Received message: {message}")
    logger.error(f"Received message: {message}")
    return make_succ_response(params)

@app.route('/api/message_v2', methods=['POST'])
def receive_message_v2():
    """
    :return: 接收消息并返回success
    """
    # 获取请求体参数
    params = request.get_json()
    logger.info(f"消息推送: {params}")

    # 返回success，告知微信服务器已经正常收到
    return "success"