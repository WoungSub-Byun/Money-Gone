# 4. 카테고리별 소비 비율
def ratio_by_category(self):
    listed_result = list(self.consumption_by_category.items())

    ratio_by_category = dict()
    for data in listed_result:
        ratio_by_category[data[0]] = round((data[1] * -1) / total_consumption, 2)

    ratio = list(ratio_by_category.values())
    labels = list(ratio_by_category.keys())

    f = plt.figure(figsize=(25, 7))
    plt.pie(ratio, labels=labels, autopct="%.1f%%")
    plt.title("Consumption ratio by category.")
    plt.show()
