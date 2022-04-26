
from math import *


from django.contrib.sites import requests


def functionsqrt(a: float, b: float, c: float):
    res = ''
    if b**2 - 4*a*c < 0:
        res = 'Equation is unsolvable'
        return res
    res = 0
    if b**2 - 4*a*c == 0:
        res = -b/(2*a)
        return res
    res = []
    if b**2 - 4*a*c > 0:
        x1 = (-b + sqrt(b**2 - 4*a*c)/(2*a))
        res.append(x1)
        x2 = (-b - sqrt(b**2 - 4*a*c)/(2*a))
        res.append(x2)
        return res
# # x = functionsqrt(a, b, c)
# con = sqlite3.connect(r'/home/alberdinamariya/PycharmProjects/squrtequations/sqrtfirst/db.sqlite3')
# cur = con.cursor()
#
# if x == 'Equation is unsolvable':
#     x = (x,)
#     cur.execute("""INSERT into squrteq_forsqrt (unsolvable) VALUES(?);""", x)
#     con.commit()
#
# elif type(x) == list:
#     x = tuple(x)
#     cur.execute("""INSERT into squrteq_forsqrt (res_1, res_2) VALUES(?, ?);""", x)
#     con.commit()
#
# elif type(x) == float:
#     x = (x,)
#     cur.execute("""INSERT into squrteq_forsqrt (res_1) VALUES(?);""", x)
#     con.commit()



# import requests
#
# ans = requests.get('http://127.0.0.1:8000/API/numberlist')






