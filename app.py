from flask import Flask, render_template, request
import csv

app = Flask(__name__)


def load_content():
    content = []

    with open("data/content.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            content.append(row)

    return content


@app.route("/")
def home():
    content = load_content()
    return render_template("index.html", content=content)


@app.route("/search")
def search():
    query = request.args.get("q", "").lower()

    content = load_content()

    results = []

    for item in content:
        if (
            query in item["title"].lower()
            or query in item["content"].lower()
            or query in item["category"].lower()
        ):
            results.append(item)

    return render_template(
        "index.html",
        content=results,
        search_query=query
    )


if __name__ == "__main__":
    app.run(debug=True)
