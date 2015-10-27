#!usr/bin/env python3
import hashlib
db={
    'michael':'e10adc3949ba59abbe56e057f20f883e',
    'bob':'878ef96e86145580c38c87f0410ad153',
    'alice':'99b1c2188db85afee403b1536010c2c9'
}
def calc_md5(password):
    md5=hashlib.md5()
    md5.update(password.encode('utf-8'))
    print(md5.hexdigest())
    return md5.hexdigest()
def login(user,password):
    if user in db:
        if  db[user]==calc_md5(password):
            print('Login successfully!')
    else:
        print('There is no one who\'s name is %s' % user)

if __name__=='__main__':
    login('alice','99b1c2188db85afee403b1536010c2c9')
    login('messi','aldjlfdjljdsfj')
