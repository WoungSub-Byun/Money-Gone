from re import template
import mpld3


def export_html(plot, title):
    title = title[10:]
    source = mpld3.fig_to_html(plot, figid="{}_id".format(title))
    is_initial = False
    is_plot_included = False
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
                    is_plot_included = True
                    end = i
                    break
                if title + "_id" in data:
                    start = i
                    status = True
    except FileNotFoundError as e:
        print(e)
        is_initial = True
    with open("/data/index.html", "w+", encoding="utf-8") as fw:
        if is_initial:
            fw.writelines(source)
        elif is_plot_included:
            templates[start : end - 1] = source
            fw.writelines(templates)
        else:
            templates.append(source)
            fw.writelines(templates)
