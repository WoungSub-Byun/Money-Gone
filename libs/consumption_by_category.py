import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 카테고리별 소비액
def consumption_by_category(df):
    categories = list(set(df["Category"]))

    consumption_by_category = dict()
    for x in categories:
        consumption_by_category[x] = 0

    for _, data in df.iterrows():
        if data["Price(\)"] < 0:
            consumption_by_category[data["Category"]] += data["Price(\)"] * -1
    df_monthly_consumption_by_category = pd.DataFrame(
        list(consumption_by_category.items())
    )

    x = np.arange(len(df_monthly_consumption_by_category[1]))

    f = plt.figure(figsize=(20, 5))
    plt.bar(x, df_monthly_consumption_by_category[1])
    plt.xticks(x, df_monthly_consumption_by_category[0])
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
    plt.title("Monthly consumption by category")
    plt.xlabel("Category")
    plt.ylabel("Price of Consumption")
    plt.show()
