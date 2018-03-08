import redis

r = redis.Redis(
    host='localhost',
    port=6379, 
    password='')

def get_redis():
    return r