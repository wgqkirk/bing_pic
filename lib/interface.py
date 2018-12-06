#!/user/bin/env.python
# _*_ coding;utf-8 _*_


from flask import Flask,jsonify,abort
from get_bing_pic_api.lib.tools import conn_mysql_check_test
server = Flask(__name__)


@server.route('/error')
def error():
    abort(404)

@server.route('/getPicUrl',methods =['get'])
def getPicUrl():
    sql='SELECT * FROM `bing_pic` ORDER BY RAND() LIMIT 1'

    res=conn_mysql_check_test(sql)
    print(res)
    return jsonify({'url':res[0]['url']})