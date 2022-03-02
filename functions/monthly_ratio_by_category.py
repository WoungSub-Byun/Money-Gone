import matplotlib.pyplot as plt
from datetime import datetime
from .total_consumption import total_consumption

# 이번달 카테고리별 소비 비율
def monthly_ratio_by_category(df):

    current_month = datetime.now().strftime("%Y-%m")

    categories = list(set(df["Category"]))

    consumption_by_category = dict()

    for x in categories:
        consumption_by_category[x] = 0

    for _, data in df.iterrows():
        if data["Price(\)"] < 0 and current_month in data["Date"]:
            consumption_by_category[data["Category"]] += data["Price(\)"] * -1

    listed_result = list(consumption_by_category.items())

    ratio_by_category = dict()
    for data in listed_result:
        ratio_by_category[data[0]] = round((data[1] * -1) / total_consumption, 2)

    ratio = list(ratio_by_category.values())
    labels = list(ratio_by_category.keys())
    f = plt.figure(figsize=(30, 8))
    plt.pie(ratio, labels=labels, autopct="%.1f%%")
    plt.title("Consumption ratio by category on Current Month.")
    return f
