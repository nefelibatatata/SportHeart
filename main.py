import pandas as pd
from db import SportDB
import time, json
import pymysql
import matplotlib.pyplot as plt
import datetime


def main():
    # csv数据太多，限制读取数量
    data = pd.read_csv("data/sportheartinfo.csv",
                       nrows=1000,
                       dtype={'学籍号': str})
    array = data['心率'][1].split(',')

    for i in range(0, int(len(array) / 2) * 2, 2):

        time_local = time.localtime(int(array[i]) / 1000)
        time.strftime("%Y-%m-%d %H:%M:%S", time_local)
        print(
            time.strftime("%Y-%m-%d %H:%M:%S", time_local) + ": " +
            array[i + 1])
    # print(data.dtypes)


def mariadb():
    db = pymysql.connect(host='localhost',
                         user='golang',
                         password='123456',
                         database='sport')
    cursor = db.cursor()
    sql = 'select * from sportheartinfo where state=1 order by rand() limit 16;'
    fig = plt.figure()
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        count = 1
        for row in results:
            # print(row)
            ax = fig.add_subplot(4, 4, count)
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
    except Exception as e:
        print(e)
    # row_array = data[:-1].split(",")
    # time_serial = row_array[0::2]
    # for i in range(len(time_serial)):
    #     time_serial[i] = time.strftime(
    #         "%Y-%m-%d %H:%M:%S", time.localtime(int(time_serial[i]) / 1000))
    # rate = row_array[1::2]
    # print(row_array)
    # print(time_serial)
    # print(rate)
    # plt.plot(time_serial, rate)
    plt.show()


def filter1():
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
            if len(row_array) < 120:
                print(data + " length: " + str(len(row_array)))
                print(disabled_sql + str(id) + ";")
                cursor.execute(disabled_sql + str(id) + ";")
                db.commit()
    except Exception as e:
        print(e)
    db.close()


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


def test():
    data = pd.read_csv("data/sportheartinfo.csv",
                       nrows=1000,
                       dtype={'学籍号': str})
    array = list(set(data['学籍号']))
    print(len(array))


if __name__ == '__main__':
    db_config = None
    with open("config/db_config.json", "r") as load_f:
        db_config = json.load(load_f)
        print(db_config)
    sportDB = SportDB(db_config)