from flask import Flask, render_template


app = Flask(__name__)


@app.route("/index", methods=["GET"])
def show_tables():
    data_dir = "/data"
    return render_template("{}/index.html".format(data_dir))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
