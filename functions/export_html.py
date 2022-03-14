import mpld3


def export_html(plot, title):
    title = title[10:]
    source = mpld3.fig_to_html(plot, figid="{}_id".format(title))
    with open("/money_gone_data/{}.html".format(title), "w+", encoding="utf-8") as f:
        f.writelines(source)
    with open("/money_gone_data/index.html", "w+", encoding="utf-8") as f:
        start, end = 0
        templates = f.readlines()
        for i, data in enumerate(templates):
            if status and ("_id" in data):
                end = i
                continue
            if title + "_id" in data:
                start = i
                status = True
        templates[start:end] = source
        f.writelines(templates)
