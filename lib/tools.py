#!/user/bin/env.python
# _*_ coding;utf-8 _*_
from get_bing_pic_api.config.setting import MYSQL_HOST,MYSQL_PORT,SQL_DB
import pymysql


def conn_mysql_check_test(sql):
    conn = pymysql.connect(host=MYSQL_HOST,user ='root',password ='newpwd',db=SQL_DB,charset='utf8',port=MYSQL_PORT)
    cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cur.execute(sql)
    res = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    return res

