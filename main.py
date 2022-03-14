import time
from flask import Flask, render_template
import load_data


app = Flask(__name__)


@app.route("/", methods=["GET"])
def show_tables():
    start_at = time.time()
    load_data.load_data()
    end_at = time.time()
    print(
        "start_at: {}\n end_at: {}\nloading time..: {}".format(
            start_at, end_at, end_at - start_at
        )
    )
    data_dir = "/app/money_gone/data/"
    return render_template("{}index.html".format(data_dir))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
