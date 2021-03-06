import pandas as pd
from db import SportDB
import time
import pymysql
import matplotlib.pyplot as plt
import datetime


def filter_time(sportDB):
    results = sportDB.getData()
    i = 0
    for row in results:
        i = i + 1
        id = row[0]
        time_serial = row[7]
        if i % 1000 == 0:
            print('第' + str(i) + '条数据，id是：' + id) #  + '\n时间序列：' + time_serial
        '''
        data_array = time_serial[:-1].split(",")
        if len(data_array) < 10 * 60 * 2:
            sportDB.disable(id)
        # table = pd.DataFrame(columns=['timestamp', 'rate'],
        #                      data=time_serial[:-1].split(","))
        # print(table)
        '''

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


def filter2(sportDB):
    disabled_sql = 'UPDATE sportheartinfo SET state=0 WHERE id='
    results = sportDB.getData()
    try:
        for row in results:
            id = row[8]
            data = row[6]
            row_array = data[:-1].split(",")
            rate_array = row_array[1::2]
            if len(set(rate_array)) <= 5:
                print(set(rate_array))
                print(disabled_sql + str(id) + ";")
                # sportDB.Execute(disabled_sql + str(id) + ";")
    except Exception as e:
        print(e)


def filter3(sportDB):
    disabled_sql = 'UPDATE sportheartinfo SET state=0 WHERE id='
    results = sportDB.getData()
    i = 0
    try:
        for row in results:
            id = row[0] # 唯一id
            data = row[7] #心率数据
            row_array = data[:-1].split(",")
            timestamp_array = row_array[::2]
            rate_array = row_array[1::2]
            timestamp_array_2 = []
            for i in range(0, len(timestamp_array)): #以1s为精度
                timestamp_array_2.append(int(timestamp_array[i]) // 1000 - int(timestamp_array[0]) // 1000)

            if len(set(timestamp_array_2)) < len(timestamp_array_2):
                i = i+1
                print("时间戳重复（以1s为精度）！")
                print(disabled_sql + str(id) + ";")
                sportDB.Execute(disabled_sql + str(id) + ";")
        print("重复数量："+str(i))

    except Exception as e:
        print(e)



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
