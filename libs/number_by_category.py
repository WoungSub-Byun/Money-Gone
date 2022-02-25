import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 카테고리별 소비 건수
def number_by_category(df):
    number_by_category = dict()
    categories = list(set(df["Category"]))
    for x in categories:
        number_by_category[x] = 0

    for _, data in df.iterrows():
        number_by_category[data["Category"]] += 1

    df_number_of_category = pd.DataFrame(list(number_by_category.items()))

    x = np.arange(len(df_number_of_category[1]))
    f = plt.figure(figsize=(20, 5))
    plot = plt.bar(x, df_number_of_category[1])
    plt.xticks(x, df_number_of_category[0])
    # 막대 위에 값 표시
    for rect in plot:
        height = rect.get_height()
        plt.text(
            rect.get_x() + rect.get_width() / 2.0,
            height,
            "%d" % height,
            ha="center",
            va="bottom",
            size=12,
        )
    plt.title("Number of Monthly Consumption by Category")
    plt.xlabel("Category")
    plt.ylabel("Amount")

    return f
