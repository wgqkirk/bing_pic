#!/user/bin/env.python
# _*_ coding;utf-8 _*


import os,sys
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
F_PATH=os.path.abspath(os.path.join(os.getcwd(), "../.."))
sys.path.insert(0,F_PATH)

from get_bing_pic_api.lib.interface import server
from get_bing_pic_api.config.setting import SERVER_PORT

#
#
#
server.config['JSON_AS_ASCII'] = False#解决中文乱码问题
server.run(host='0.0.0.0',port=SERVER_PORT,debug=True)