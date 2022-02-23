import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import gdown
import configparser
import mpld3

# 한글 폰트 설치
# !sudo apt-get install -y fonts-nanum
# !sudo fc-cache -fv
# !rm ~/.cache/matplotlib -rf

# mpld로 html 출력
# mpld3.fig_to_html(f, figid='THIS_IS_FIGID')


def load_dataset():
    config = configparser.ConfigParser()
    config.read("./config.ini", encoding="utf-8")
    config.sections()

    google_path = "https://drive.google.com/uc?id="
    file_id = config["link"]["file_id"]
    output_name = config["link"]["file_name"]

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


def boot():
    # matplotlib 한글 폰트 적용
    plt.rc("font", family="NanumBarunGothic")

    df = load_dataset()
    print(df)


boot()
