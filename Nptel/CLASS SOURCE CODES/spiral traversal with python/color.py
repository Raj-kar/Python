import random

def gen_color():
    color = ["#" + ''.join([random.choice('0123456789ABCDEF')
                            for j in range(6)])]
    return color[0]
