import pymysql
from config import  host, user, password, db_name


try:
    connection = pymysql.connect(
        host=host,
        port=3306,
        user=user,
        password=password,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor
    )
    print("successfully connected...")
    print("#" * 20)

    try:
        # cursor = connection.cursor()

        with connection.cursor() as cursor:

    finally:
        connection.close()

except Exception as ex:
    print("Connection refused...")
    print(ex)