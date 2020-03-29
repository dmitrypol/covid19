''' services '''
from . import REDIS_CLIENT


def get_data():
    keys = REDIS_CLIENT.keys('*')
    output = []
    for key in keys:
        output.append(REDIS_CLIENT.hgetall(key))
    return output
