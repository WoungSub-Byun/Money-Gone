import mpld3


def export_html(plot, title):
    title = title[10:]
    source = mpld3.fig_to_html(plot, figid="{}_id".format(title))
    with open("/app/money_gone/data/{}.txt".format(title), "w", encoding="utf-8") as f:
        f.writelines(source)
