#!/user/bin/env.python
# _*_ coding;utf-8 _*_


from flask import Flask, jsonify, abort, request
from get_bing_pic_api.lib.tools import conn_mysql_check_test
from get_bing_pic_api.config.setting import WECHAT_TOKEN
server = Flask(__name__)
import hashlib


@server.route('/error')
def error():
    abort(404)


@server.route('/getPicUrl',methods =['get'])
def getPicUrl():
    signature=request.args.get("signature")
    timestamp=request.args.get("timestamp")
    nonce=request.args.get("nonce")
    echostr=request.args.get("echostr")
    token=WECHAT_TOKEN
    list = [token, timestamp, nonce]
    list.sort()
    temp = ''.join(list)
    print(signature,timestamp,nonce,echostr)
    final_str=hashlib.sha1(temp.encode('utf8')).hexdigest()
    print(final_str)
    print(signature)
    if final_str==signature:
        return echostr
    sql='SELECT * FROM `bing_pic` ORDER BY RAND() LIMIT 1'
    res=conn_mysql_check_test(sql)
    print(res)
    return jsonify({'url':res[0]['url']})