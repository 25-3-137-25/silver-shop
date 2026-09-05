from flask import Flask, render_template

app = Flask(__name__)


PRODUCTS = [
    {
        "id": 1,
        "title": "Кольцо Liquid Silver",
        "category": "Кольца",
        "price": "5 400 ₽",
        "tag": "Серебро 925",
        "image": "liqring.jpg",
    },
    {
        "id": 2,
        "title": "Кафф Minimal Edge",
        "category": "Серьги",
        "price": "3 800 ₽",
        "tag": "Серебро 925",
        "image": "kaff.jpg",
    },
    {
        "id": 3,
        "title": "Цепь Raw Link",
        "category": "Цепи",
        "price": "8 200 ₽",
        "tag": "Черненое серебро",
        "image": "cep.jpg",
    },
]


@app.route("/")
def index():
    return render_template("index.html", products=PRODUCTS)


@app.route("/catalog")
def catalog():
    return render_template("catalog.html", products=PRODUCTS)


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)