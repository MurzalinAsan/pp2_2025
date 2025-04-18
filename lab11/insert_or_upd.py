import psycopg2
from insertfromterminal import insert_vendor
from checkexistence import name_exists
from update import update

name = input("name: ")
phone_num = input("num: ")

if name_exists(name):
    update(name, phone_num)
else:
    insert_vendor(name, phone_num)