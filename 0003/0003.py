# coding=utf-8

import uuid
import redis

"""
003, 将 0001 题生成的 200 个激活码（或者优惠券）保存到 **Redis** 非关系型数据库中.
参考材料
format使用
http://www.jb51.net/article/63672.htm
windows 安装redis
http://www.biaodianfu.com/windows-redis-python.html
"""


class save_keys_redis:

    def __init__(self):
        self.redis = redis.StrictRedis(host='localhost', port=6379)
        self.code_list = []

    def generate_activation_code(self, count):
        for i in xrange(count):
            code = str(uuid.uuid1()).replace('-', '')
            if not code in self.code_list:
                self.code_list.append(code)

    def store_to_redise(self):
        if self.code_list:
            cache = self.redis
            try:
                cache.set('code:count', len(self.code_list))
                for i in xrange(len(self.code_list)):
                    cache.set('code:{0}'.format(i), self.code_list[i])
                cache.save()
                return True
            except:
                print 'Can not connect to redis server !!!'

        return False

    def print_activation_code(self):
        cache = self.redis
        try:
            count = cache.get('code:count')

            count = 0 if count is None else int(count)

            for i in xrange(count):
                print i, cache.get('code:%d' % i)
        except:
            print 'Can not connect to redis server !!!'

test = save_keys_redis()
test.generate_activation_code(200)
if test.store_to_redise():
    test.print_activation_code()
