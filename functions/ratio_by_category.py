from .total_consumption import total_consumption
import matplotlib.pyplot as plt
from .export_html import export_html

#  카테고리별 소비 비율
def ratio_by_category(df):
    categories = list(set(df["Category"]))

    consumption_by_category = dict()
    for x in categories:
        consumption_by_category[x] = 0

    for _, data in df.iterrows():
        if data["Price(\)"] < 0:
            consumption_by_category[data["Category"]] += data["Price(\)"] * -1
    listed_result = list(consumption_by_category.items())

    ratio_by_category = dict()
    for data in listed_result:
        ratio_by_category[data[0]] = round((data[1] * -1) / total_consumption(df), 2)

    ratio = list(ratio_by_category.values())
    labels = list(ratio_by_category.keys())
    if sum(ratio) == 0:
        print("There's no data")
        return
    f = plt.figure(figsize=(25, 7))
    plt.pie(ratio, labels=labels, autopct="%.1f%%")
    plt.title("Consumption ratio by category.")
    export_html(f, __name__)
