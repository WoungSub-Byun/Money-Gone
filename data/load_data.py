import gdown
import configparser
import matplotlib.pyplot as plt
import pandas as pd

from functions import *

# 한글 폰트 설치
# !sudo apt-get install -y fonts-nanum
# !sudo fc-cache -fv
# !rm ~/.cache/matplotlib -rf

# mpld로 html 출력
# mpld3.fig_to_html(f, figid='THIS_IS_FIGID')


def load_dataset():
    # config = configparser.ConfigParser()
    # config.read("./config.ini", encoding="utf-8")

    google_path = "https://drive.google.com/uc?id="
    file_id = "1jCjpni5onM8DThulWYKx4UIvKHi1Aqf3"
    output_name = "accountbook.xlsx"

    gdown.download(google_path + file_id, output_name, quiet=True)

    names = ["Date", "Category", "Where", "Reason", "Price(\)"]
    org_dataset = pd.read_excel(
        output_name,
        sheet_name=0,
        header=3,
        names=names,
    )
    df = pd.DataFrame()
    for idx, data in org_dataset.iterrows():
        df[idx] = data
        df[idx]["Date"] = str(data["Date"].strftime("%Y-%m-%d"))
    df = df.transpose()
    df = df.fillna("")
    return df


def load_data():
    # matplotlib 한글 폰트 적용
    plt.rc("font", family="NanumBarunGothic")

    df = load_dataset()

    # avg_meal_consumption(df)
    # max_by_category(df)
    # monthly_consumption(df)
    # today_consumption(df)
    # total_consumption(df)

    consumption_by_category(df)
    current_daily_consumption(df)
    daily_consumption(df)
    monthly_daily_consumption(df)
    monthly_ratio_by_category(df)
    number_by_category(df)
    ratio_by_category(df)


load_data()
