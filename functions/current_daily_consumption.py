from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from .export_html import export_html

# 최근 30일간 일별 소비액
def current_daily_consumption(df):
    timestamps = list(set(df["Date"]))
    today = datetime.now()

    daily_consume = dict()

    for day in timestamps:
        daily_consume[day] = 0

    for _, value in df.iterrows():
        if (
            value["Price(\)"] < 0
            and (today - datetime.strptime(value["Date"], "%Y-%m-%d")).days < 30
        ):
            daily_consume[value["Date"]] += value["Price(\)"] * -1

    df_daily_consumption = pd.DataFrame(list(daily_consume.items()))

    # 일자별로 정렬하기
    df_dc = df_daily_consumption.sort_values(by=df_daily_consumption.columns[0])

    x = np.arange(len(df_dc[1]))

    f = plt.figure(figsize=(20, 5))

    plot = plt.bar(x, df_dc[1])
    plt.xticks(x, df_dc[0])

    # 막대 위에 값 표시
    for rect in plot:
        height = rect.get_height()
        plt.text(
            rect.get_x() + rect.get_width() / 2.0,
            height,
            "%.1f" % height,
            ha="center",
            va="bottom",
            size=12,
        )
    plt.title("Daily consumption trend On Current 30days ({})".format(today))
    plt.xlabel("Date")
    plt.ylabel("Daily Consumption")
    export_html(f, __name__)
