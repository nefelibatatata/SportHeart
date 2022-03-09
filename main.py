import pandas as pd
from db import SportDB
import time
import pymysql
import matplotlib.pyplot as plt
import datetime


def filter_time(sportDB):
    results = sportDB.getData(1)
    for row in results:
        # id = row[0]
        time_serial = row[7]
        print(time_serial)
        # table = pd.DataFrame(columns=['timestamp', 'rate'],
        #                      data=time_serial[:-1].split(","))
        # print(table)


def show_chart(sportDB):

    fig = plt.figure()
    count = 1
    ax = fig.add_subplot(4, 4, count)
    results = sportDB.getData()
    for row in results:
        # print(row)

        count += 1
        data = row[7]
        row_array = data[:-1].split(",")
        time_serial = row_array[0::2]
        # for i in range(len(time_serial)):
        #     time_serial[i] = time.strftime(
        #         "%Y-%m-%d %H:%M:%S",
        #         time.localtime(int(time_serial[i]) / 1000))
        rate = row_array[1::2]
        time_serial = [int(str(x)) / 1000 for x in time_serial]
        rate = [int(str(x)) for x in rate]
        # # print(time_serial)
        # # print(rate)
        # for i in range(len(time_serial)):
        #     print(time_serial[i] + ": " + rate[i])
        # print("---------------------")
        ax.scatter(time_serial, rate)
    plt.show()


def main():
    sportDB = SportDB()
    filter_time(sportDB)


def filter2():
    db = pymysql.connect(host='localhost',
                         user='golang',
                         password='123456',
                         database='sport')
    cursor = db.cursor()
    sql = 'select * from sportheartinfo where state=1;'
    disabled_sql = 'UPDATE sportheartinfo SET state=0 WHERE id='
    results = None
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()

    except Exception as e:
        print(e)

    try:
        for row in results:
            # print(row)
            id = row[0]
            data = row[7]
            row_array = data[:-1].split(",")
            rate_array = row_array[1::2]
            if len(set(rate_array)) <= 5:
                print(set(rate_array))
                print(disabled_sql + str(id) + ";")
                cursor.execute(disabled_sql + str(id) + ";")
                db.commit()
    except Exception as e:
        print(e)
    db.close()


# 文本中提取时间序列
def transform_text_to_serial(text):

    row_array = text[:-1].split(",")
    time_serial = row_array[0::2]
    # for i in range(len(time_serial)):
    #     time_serial[i] = time.strftime(
    #         "%Y-%m-%d %H:%M:%S",
    #         time.localtime(int(time_serial[i]) / 1000))
    rate = row_array[1::2]
    # print(time_serial)
    # print(rate)
    for i in range(len(time_serial)):
        print(time_serial[i] + ": " + rate[i])


def filter_old():
    db = pymysql.connect(host='localhost',
                         user='golang',
                         password='123456',
                         database='sport')
    cursor = db.cursor()
    sql = 'select * from sportheartinfo where state=1;'
    disabled_sql = 'UPDATE sportheartinfo SET state=0 WHERE id='
    results = None
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()

    except Exception as e:
        print(e)

    try:
        for row in results:
            # print(row)
            id = row[0]
            date = row[3]
            if date < datetime.date(2021, 9, 1):
                print(date)
                cursor.execute(disabled_sql + str(id) + ";")
                db.commit()
    except Exception as e:
        print(e)
    db.close()


if __name__ == '__main__':
    main()
