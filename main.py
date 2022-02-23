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

# mpld로 html 출력
# mpld3.fig_to_html(f, figid='THIS_IS_FIGID')


def load_dataset():
    names = ["Date", "Category", "Where", "Reason", "Price(\)"]
    org_dataset = pd.read_excel(
        "/content/drive/MyDrive/가계부/웅섭이의 소비생활 파헤치기.xlsx",
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


def main():
    # matplotlib 한글 폰트 적용
    plt.rc("font", family="NanumBarunGothic")

    df = load_dataset()


class Main:
    def __init__(self) -> None:

        # matplotlib 한글 폰트 적용
        plt.rc("font", family="NanumBarunGothic")
        self.df = self.load_dataset()

    # # 13. 이번달 주별 소비액

    # today = datetime.today()

    # current_month_week = datetime.today().weekday()

    # for _, data in self.df.iterrows():
    #   if current_month in data['Date'] and datetime.strptime(data['Date'], "%Y-%m-%d") <= today:
    #     tmp_date = datetime.strptime(data['Date'], "%Y-%m-%d")
    #     if tmp_date.weekday()
