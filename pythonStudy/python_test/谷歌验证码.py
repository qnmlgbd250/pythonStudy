# -*- coding: utf-8 -*-
# @Time    : 2021/12/15 20:19
# @Author  : sunfukai
# @Email   : zcshiyonghao@163.com
# @File    : 谷歌验证码.py
# @Software: PyCharm
def google_code():
    import hmac, base64, struct, hashlib, time
    secret_key = 'XXUMZM2S26JV3YIJ'  # 谷歌身份验证秘钥
    if secret_key:
        current_time = int(time.time()) // 30  # 每30秒更新一次
        key = base64.b32decode(secret_key)
        msg = struct.pack(">Q", current_time)
        google_code = hmac.new(key, msg, hashlib.sha1).digest()
        o = ord(chr(google_code[19])) & 15  # python3时，ord的参数必须为chr类型
        google_code = (struct.unpack(">I", google_code[o:o + 4])[0] & 0x7fffffff) % 1000000
        return '%06d' % google_code  # 不足6位时，在前面补0
    else:
        return '000000'

if __name__ == '__main__':
    print(google_code())