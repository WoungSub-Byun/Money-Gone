from datetime import datetime

# 오늘 총 소비액
def today_consumption(df):
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
