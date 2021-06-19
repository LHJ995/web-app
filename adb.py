import pymysql

def insert_user(userid, username, userpw):
    db = pymysql.connect(host='localhost', user='root', password='1234', db='adb', charset='utf8')
    c = db.cursor()
    setdata = (userid, userpw, username)
    c.execute("INSERT INTO user VALUES (%s, %s, %s)", setdata)
    db.commit()

def get_user(userid, userpw):
    ret = ()
    try:
        db = pymysql.connect(host='localhost', user='root', password='1234', db='adb', charset='utf8')
        c = db.cursor()
        setdata = (userid, userpw)
        c.execute('SELECT * FROM user WHERE userid = %s AND userpw = %s', setdata)
        ret = c.fetchone()
    except Exception as e:
        print('db error:', e)
    finally:
        db.close()
        return ret

#ret = get_user('aaa', '1234')
#print(ret)

#if ret != None:
    #print(ret)
#else:
    #print("확인")