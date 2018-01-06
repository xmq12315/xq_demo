from hashlib import md5

def PwdToMd5(pwd):
    pwd = md5(pwd.encode('utf-8'))
    pwd2 = pwd.hexdigest()
    return pwd2


if __name__ == '__main__':
    print(PwdToMd5('1'))
