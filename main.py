import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import time
import mpld3

# 한글 폰트 설치
# !sudo apt-get install -y fonts-nanum
# !sudo fc-cache -fv
# !rm ~/.cache/matplotlib -rf

# matplotlib 한글 폰트 적용
plt.rc("font", family="NanumBarunGothic")

# 데이터셋 읽어오기
names = ["Date", "Category", "Where", "Reason", "Price(\)"]
org_df = pd.read_excel(
    "/content/drive/MyDrive/가계부/웅섭이의 소비생활 파헤치기.xlsx",
    sheet_name=0,
    header=3,
    names=names,
)
df = pd.DataFrame()
for idx, data in org_df.iterrows():
    df[idx] = data
    df[idx]["Date"] = str(data["Date"].strftime("%Y-%m-%d"))
df = df.transpose()
df = df.fillna("")
df


# 1. 일별 소비액
def daily_consumption():
    timestamps = list(set)(df["Date"])

    daily_consume = dict()
    for day in timestamps:
        daily_consume[day] = 0

    for _, value in df.iterrows():
        if value["Price(\)"] < 0:
            daily_consume[value["Date"]] += value["Price(\)"] * -1

    df_daily_consumption = pd.DataFrame(list(daily_consume.items()))

    # 일자별로 정렬하기
    df_dc = df_daily_consumption.sort_values(by=df_daily_consumption.columns[0])

    x = np.arange(len(df_daily_consumption[1]))

    f = plt.figure(figsize=(20, 5))

    plot = plt.bar(x, df_daily_consumption[1])
    plt.xticks(x, df_daily_consumption[0])

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
    plt.title("Daily consumption trend.")
    plt.xlabel("Date")
    plt.ylabel("Daily Consumption")
    plt.show()


# mpld로 html 출력
# mpld3.fig_to_html(f, figid='THIS_IS_FIGID')

# 2. 총 소비액
def total_consumption():

    total_consumption = 0
    for consumption in df["Price(\)"]:
        if consumption < 0:
            total_consumption += consumption

    print("총 소비액(원): {}원".format(total_consumption))


# 3. 카테고리별 소비액
def consumption_by_category():
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


# 4. 카테고리별 소비 비율
def ratio_by_category():
    listed_result = list(consumption_by_category.items())

    ratio_by_category = dict()
    for data in listed_result:
        ratio_by_category[data[0]] = round((data[1] * -1) / total_consumption, 2)

    ratio = list(ratio_by_category.values())
    labels = list(ratio_by_category.keys())

    f = plt.figure(figsize=(25, 7))
    plt.pie(ratio, labels=labels, autopct="%.1f%%")
    plt.title("Consumption ratio by category.")
    plt.show()


# 5. 카테고리별 소비 건수
def number_by_category():
    number_by_category = dict()

    for x in categories:
        number_by_category[x] = 0

    for _, data in df.iterrows():
        number_by_category[data["Category"]] += 1

    df_number_of_category = pd.DataFrame(list(number_by_category.items()))

    x = np.arange(len(df_number_of_category[1]))

    plt.bar(x, df_number_of_category[1])
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
    plt.show()


# 6. 각 카테고리별 최대 소비액 데이터
def max_by_category():
    max_by_category = dict()

    for x in categories:
        max_by_category[x] = 0

    for _, data in df.iterrows():
        if (
            data["Price(\)"] < 0
            and max_by_category[data["Category"]] > data["Price(\)"]
        ):
            max_by_category[data["Category"]] = data["Price(\)"]

    colnames = ["Category", "Price(\)"]
    categorical_max_df = pd.DataFrame(list(max_by_category.items()), columns=colnames)
    categorical_max_df.set_index("Category", inplace=True)
    print("# Maximum consumption for each category.")
    return categorical_max_df


# 7. 아침, 점심, 저녁 평균 소비 금액
def avg_meal_consumption():
    meal_category = ["breakfast", "lunch", "dinner"]

    meal_category_sum = dict()
    meal_category_cnt = dict()
    for meal in meal_category:
        meal_category_sum[meal] = 0
        meal_category_cnt[meal] = 0

    # 데이터 셋 중에 category가 식비 인 것 and 사용처가 아침식사, 점심식사, 저녁식사 셋 중 하나라도 '포함되는' 문자열일 경우 해당 문자열이 key인 내용에 추가, 개수 카운트
    for _, data in df.iterrows():
        if data["Category"] == "식비":
            if "아침식사" in data["Reason"]:
                meal_category_sum["breakfast"] += data["Price(\)"]
                meal_category_cnt["breakfast"] += 1
            if "점심식사" in data["Reason"]:
                meal_category_sum["lunch"] += data["Price(\)"]
                meal_category_cnt["lunch"] += 1
            if "저녁식사" in data["Reason"]:
                meal_category_sum["dinner"] += data["Price(\)"]
                meal_category_cnt["dinner"] += 1

    meal_category_avg = dict()
    for key, value in meal_category_sum.items():
        if meal_category_cnt[key] == 0:
            continue
        meal_category_avg[key] = round(
            (meal_category_sum[key] * -1) / meal_category_cnt[key], 1
        )

    result_list = np.array(
        [
            list(meal_category_avg.keys()),
            list(meal_category_avg.values()),
            list(meal_category_cnt.values()),
        ]
    )

    colnames = ["Meals", "Avg Price(\)", "Number"]
    meal_category_avg_df = pd.DataFrame(result_list.T, columns=colnames)
    meal_category_avg_df.set_index("Meals", inplace=True)
    return meal_category_avg_df


# 8. 오늘 총 소비액
def today_consumption():
    today = datetime.now().strftime("%Y-%m-%d")
    today_consumption = 0
    today_income = 0
    for _, value in df.iterrows():
        if value["Date"] == today:
            if value["Price(\)"] < 0:
                today_consumption += value["Price(\)"]
            else:
                today_income += value["Price(\)"]
    print(" 오늘 총 소비액: {}원\n 오늘 총 수입: {}원".format(today_consumption, today_income))


# 9. 이번달 일별 소비액
def daily_consumption():

    timestamps = list(set(df["Date"]))
    current_month = datetime.now().strftime("%Y-%m")
    daily_consume = dict()
    for day in timestamps:
        daily_consume[day] = 0

    for _, value in df.iterrows():
        if value["Price(\)"] < 0 and current_month in value["Date"]:
            daily_consume[value["Date"]] += value["Price(\)"] * -1

    df_daily_consumption = pd.DataFrame(list(daily_consume.items()))

    # 일자별로 정렬하기
    df_dc = df_daily_consumption.sort_values(by=df_daily_consumption.columns[0])

    x = np.arange(len(df_daily_consumption[1]))

    f = plt.figure(figsize=(20, 5))

    plot = plt.bar(x, df_daily_consumption[1])
    plt.xticks(x, df_daily_consumption[0])

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
    plt.title("Daily consumption trend ({})".format(current_month))
    plt.xlabel("Date")
    plt.ylabel("Daily Consumption")
    plt.show()
    # mpld로 html 출력
    # mpld3.fig_to_html(f, figid='THIS_IS_FIGID')


# 10. 최근 30일간 일별 소비액
def current_daily_consumption():
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

    x = np.arange(len(df_daily_consumption[1]))

    f = plt.figure(figsize=(20, 5))

    plot = plt.bar(x, df_daily_consumption[1])
    plt.xticks(x, df_daily_consumption[0])

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
    plt.show()
    # mpld로 html 출력
    # mpld3.fig_to_html(f, figid='THIS_IS_FIGID')


# 11. 이번달 총 소비액
def monthly_consumption():

    current_month = datetime.now().strftime("%Y-%m")

    current_month_total_consumption = 0

    for _, value in df.iterrows():
        if value["Price(\)"] < 0 and current_month in value["Date"]:
            current_month_total_consumption += value["Price(\)"] * -1

    print("이번달 총 소비액: {}원".format(current_month_total_consumption))


# 12. 이번달 카테고리별 소비 비율
def monthly_ratio_by_category():

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
    plt.show()


# # 13. 이번달 주별 소비액

# today = datetime.today()

# current_month_week = datetime.today().weekday()

# for _, data in df.iterrows():
#   if current_month in data['Date'] and datetime.strptime(data['Date'], "%Y-%m-%d") <= today:
#     tmp_date = datetime.strptime(data['Date'], "%Y-%m-%d")
#     if tmp_date.weekday()
