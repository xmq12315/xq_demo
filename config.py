import os
DIVER = 'mysql'
QD_DIVER = 'pymysql'
USER = 'root'
PASSWORD = 'root'
HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'test'
SQLALCHEMY_DATABASE_URI = '{}+{}://{}:{}@{}:{}/{}'.format(DIVER, QD_DIVER, USER, PASSWORD, HOST, PORT, DATABASE)
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY=os.urandom(24)


# import os
# DIVER = 'mysql'
# QD_DIVER = 'pymysql'
# USER = 'qdm163951500'
# PASSWORD = 'nm160602'
# HOST = 'qdm163951500.my3w.com'
# PORT = '3306'
# DATABASE = 'qdm163951500_db'
# SQLALCHEMY_DATABASE_URI = '{}+{}://{}:{}@{}:{}/{}'.format(DIVER, QD_DIVER, USER, PASSWORD, HOST, PORT, DATABASE)
# SQLALCHEMY_TRACK_MODIFICATIONS = True
# SECRET_KEY=os.urandom(24)

if __name__ == '__main__' :
    print(SQLALCHEMY_DATABASE_URI)