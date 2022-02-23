# 7. 아침, 점심, 저녁 평균 소비 금액
def avg_meal_consumption(self):
    meal_category = ["breakfast", "lunch", "dinner"]

    meal_category_sum = dict()
    meal_category_cnt = dict()
    for meal in meal_category:
        meal_category_sum[meal] = 0
        meal_category_cnt[meal] = 0

    # 데이터 셋 중에 category가 식비 인 것 and 사용처가 아침식사, 점심식사, 저녁식사 셋 중 하나라도 '포함되는' 문자열일 경우 해당 문자열이 key인 내용에 추가, 개수 카운트
    for _, data in self.df.iterrows():
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
