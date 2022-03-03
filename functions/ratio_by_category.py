from .consumption_by_category import consumption_by_category
from .total_consumption import total_consumption
import matplotlib.pyplot as plt
from .export_html import export_html

#  카테고리별 소비 비율
def ratio_by_category(df):
    listed_result = list(consumption_by_category.items())

    ratio_by_category = dict()
    for data in listed_result:
        ratio_by_category[data[0]] = round((data[1] * -1) / total_consumption, 2)

    ratio = list(ratio_by_category.values())
    labels = list(ratio_by_category.keys())

    f = plt.figure(figsize=(25, 7))
    plt.pie(ratio, labels=labels, autopct="%.1f%%")
    plt.title("Consumption ratio by category.")
    export_html(f, "카테고리별 소비 비율")
