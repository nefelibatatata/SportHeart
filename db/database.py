import pymysql
import pandas as pd
import time
import json


class SportDB:

    def __init__(self):
        db_config = None
        with open("config/db_config.json", "r") as load_f:
            db_config = json.load(load_f)
        mysql_config = db_config['mysql']
        self.host = mysql_config['host']
        self.db = pymysql.connect(host=mysql_config['host'],
                                  user=mysql_config['user'],
                                  password=mysql_config['password'],
                                  database=mysql_config['database'])
        self.cursor = self.db.cursor()

    def disable(self, id):
        disabled_sql = 'UPDATE sportheartinfo SET state=0 WHERE id=' + str(
            id) + ";"
        print(disabled_sql)
        self.cursor.execute(disabled_sql)
        self.db.commit()

    def getData(self, number=None):
        sql = None
        if number is None:
            sql = "select * from sportheartinfo where state=1;"
        else:
            sql = "select * from sportheartinfo where state=1 order "\
                "by rand() limit %d;" % number

        print(sql)

        try:
            # 执行SQL语句
            self.cursor.execute(sql)
            # 获取所有记录列表
            results = self.cursor.fetchall()
            return results

        except Exception as e:
            print(e)

        return None

    def import_sportheartinfo(self):
        data = pd.read_csv("data/sportheartinfo.csv", dtype={'学籍号': str})
        for i in range(0, data.shape[0]):
            sql = "INSERT INTO sportheartinfo(student_id, device_id,"\
                "sport_date, start_time, sport_type, location, heart_rate"\
                ")VALUES ("

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
            self.cursor.execute(sql)
            # 提交到数据库执行
            self.db.commit()
        except Exception as e:
            print(e)
            # 如果发生错误则回滚
            self.db.rollback()

    def import_sportstatisticinfo(self):

        data = pd.read_csv(
            "data/sportstatisticinfo.csv",
            #    nrows=2,
            dtype={'学籍号': str})
        for i in range(0, data.shape[0]):
            sql = "INSERT INTO sportstatisticinfo(student_id, device_id,"\
                "sport_date,start_time, sport_type, continuing_time, steps,"\
                " calory,distance, standard_time, max_heart_rate,"\
                " average_heart_rate, max_steps, average_steps, rate)VALUES ("
            for j in range(0, data.shape[1]):
                # 转换时间格式为mysql数据库格式
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
                self.cursor.execute(sql)
                # 提交到数据库执行
                self.db.commit()
            except Exception as e:
                print(e)
                # 如果发生错误则回滚
                self.db.rollback()

    def Execute(self, sql):
        self.cursor.execute(sql)
        self.db.commit()

    def __del__(self):
        self.db.close()
