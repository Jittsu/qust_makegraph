import  datetime
import re
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def str_to_time(time_str):
    time_list = re.split("[:.]", time_str)
    if len(time_list) == 2:
        min = 0
        sec = int(time_list[0])
        micro_sec = int(time_list[1]) * (10**4)
        ans = datetime.timedelta(minutes=min, seconds=sec, microseconds=micro_sec)
        return ans
    elif len(time_list) == 3:
        min = int(time_list[0])
        sec = int(time_list[1])
        micro_sec = int(time_list[2]) * (10**4)
        ans = datetime.timedelta(minutes=min, seconds=sec, microseconds=micro_sec)
        return ans
    else:
        print("Error: 入力ミスがあります。最初から入力してください。")
        main()

def main():    
    name = input("名前を入力してください(Write Alphabet)：")
    event = input("種目名を入力してください(Write Alphabet)：")
    date = []
    time = []
    cnt = 1

    while True:
        input_date = input("{0}つ目のタイム計測日を入力(ex: 2019-01-01)：".format(cnt))
        input_time = input("{0}のタイムを入力(ex: 1:12.34)：".format(input_date))
        date.append(input_date)
        time.append(input_time)
        branch = input("入力を続けますか？(yes or no)：")
        if branch == "yes":
            cnt += 1
        elif branch == "no":
            break
        else:
            print("Error: 予期せぬ入力がありました。アプリケーションを再起動してください。")
            break

    x = [datetime.datetime.strptime(d, "%Y-%m-%d") for d in date]
    y = [str_to_time(t).total_seconds() for t in time]

    plt.style.use("seaborn")
    plt.plot(x, y)
    plt.xlabel("DATE")
    plt.ylabel("TIME")
    plt.title("{0}".format(name) + ":" + "{0}".format(event))
    plt.show()

if __name__ == "__main__":
    print("<Ver. 1.0.1: アルファベット入力のみに対応しています。>\n")
    print("古い記録から順に入力してください")
    main()
