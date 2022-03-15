import mpld3


def export_html(plot, title):
    title = title[10:]
    source = mpld3.fig_to_html(plot, figid="{}_id".format(title))
    is_initial = True
    with open("/data/{}.html".format(title), "w+", encoding="utf-8") as f:
        f.writelines(source)
    try:
        with open("/data/index.html", "r", encoding="utf-8") as fr:
            start = 0
            end = 0
            status = False
            templates = fr.readlines()
            for i, data in enumerate(templates):
                if status and ("_id" in data):
                    end = i
                    continue
                if title + "_id" in data:
                    start = i
                    status = True
    except Exception as e:
        print(e)
        is_initial = True
    with open("/data/index.html", "w+", encoding="utf-8") as fw:
        if is_initial:
            fw.writelines(source)
            is_initial = False
        else:
            templates[start:end] = source
            fw.writelines(templates)
