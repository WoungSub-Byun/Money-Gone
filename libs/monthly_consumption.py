# 11. 이번달 총 소비액
def monthly_consumption(self):

    current_month = datetime.now().strftime("%Y-%m")

    current_month_total_consumption = 0

    for _, value in self.df.iterrows():
        if value["Price(\)"] < 0 and current_month in value["Date"]:
            current_month_total_consumption += value["Price(\)"] * -1

    print("이번달 총 소비액: {}원".format(current_month_total_consumption))
