import pymysql
import pandas as pd
import time
import matplotlib.pyplot as plt


# sportheartinfo表中插入数据
def sportheartinfo():
    db = pymysql.connect(host='localhost',
                         user='golang',
                         password='123456',
                         database='sport')
    cursor = db.cursor()
    data = pd.read_csv("data/sportheartinfo.csv", dtype={'学籍号': str})
    for i in range(0, data.shape[0]):
        sql = "INSERT INTO sportheartinfo(student_id, device_id,sport_date, \
            start_time, sport_type, location, heart_rate)VALUES ("

        for j in range(0, data.shape[1]):
            if j == 2:
                local_time = time.strptime(data.iloc[i, j], "%d/%m/%Y")
                sql += '"%s",' % str(time.strftime("%Y-%m-%d", local_time))
                continue
            sql += '"%s",' % data.iloc[i, j]
        print(sql)
        sql = sql[:-1] + ');'
        print(sql)
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
        except Exception as e:
            print(e)
            # 如果发生错误则回滚
            db.rollback()


# sportstatisticinfo表中插入数据
def sportstatisticinfo():
    db = pymysql.connect(host='localhost',
                         user='golang',
                         password='123456',
                         database='sport')
    cursor = db.cursor()
    data = pd.read_csv(
        "data/sportstatisticinfo.csv",
        #    nrows=2,
        dtype={'学籍号': str})
    for i in range(0, data.shape[0]):
        sql = "INSERT INTO sportstatisticinfo(student_id, device_id,sport_date,start_time, sport_type, continuing_time, steps, calory, distance, standard_time, max_heart_rate, average_heart_rate, max_steps, average_steps, rate)VALUES ("
        for j in range(0, data.shape[1]):
            # if j == 0:
            #     sql += '%s,' % data.iloc[i, j]
            #     continue
            if j == 2:
                local_time = time.strptime(data.iloc[i, j], "%d/%m/%Y")
                sql += '"%s",' % str(time.strftime("%Y-%m-%d", local_time))
                continue
            sql += '"%s",' % data.iloc[i, j]
        print(sql)
        sql = sql[:-1] + ');'
        print(sql)
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
        except Exception as e:
            print(e)
            # 如果发生错误则回滚
            db.rollback()


if __name__ == '__main__':
    sportstatisticinfo()
