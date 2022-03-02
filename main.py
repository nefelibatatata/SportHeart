import pandas as pd
import time


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


def test():
    data = pd.read_csv("data/sportheartinfo.csv",
                       nrows=1000,
                       dtype={'学籍号': str})
    array = list(set(data['学籍号']))
    print(len(array))


if __name__ == '__main__':
    # main()
    test()
