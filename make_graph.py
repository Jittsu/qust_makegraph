import  datetime
import re
import matplotlib.pyplot as plt

def str_to_time(time_str):
    time_list = re.split("[:.]", time_str)
    if len(time_list) == 2:
        ans = datetime.datetime.strptime(time_str, '%S.%L') # error
        return ans
    elif len(time_list) == 3:
        ans = datetime.datetime.strptime(time_str, '%M:%S.%L') # error
        return ans
    else:
        print("Error: 入力ミスがあります。最初から入力してください。")
        main()

def main():
    name = input("名前を入力してください：")
    event = input("種目名を入力してください：")
    date = []
    time = []
    cnt = 1

    while True:
        input_date = input("{0}つ目のタイム計測日を入力：".format(cnt))
        input_time = input("{0}のタイムを入力：".format(input_date))
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
    y = [str_to_time(t) for t in time]

    plt.plot(x, y)
    plt.xlabel("DATE")
    plt.ylabel("TIME")
    plt.title("{0}".format(name) + "：" + "{0}".format(event))

if __name__ == "__main__":
    main()