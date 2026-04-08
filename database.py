import mysql.connector as c
def get_db():
    con=c.connect(host='localhost',user='root',password='9713',database='chemistry')
    return con