import hashlib

username = 'xmq12315'
pwd = '12315'
m=hashlib.md5(pwd.encode('utf-8'))
pwd2=m.hexdigest()
print(username)
print(pwd)
print(pwd2)
x=input("请输入密码：")
x=hashlib.md5(x.encode('utf-8'))
x2=x.hexdigest()
if x2==pwd2:
    print('密码正常')
else:
    print('密码不正确')

