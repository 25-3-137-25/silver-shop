from flask import Flask, render_template

app = Flask(__name__)

# Пример базовых данных, которые потом можно связать с базой или админкой
PRODUCTS = [
    {
        "id": 1,
        "title": "Кольцо «Liquid Silver»",
        "category": "Кольца",
        "price": "5 400 ₽",
        "tag": "Серебро 925",
    },
    {
        "id": 2,
        "title": "Кафф «Minimal Edge»",
        "category": "Серьги & Каффы",
        "price": "3 800 ₽",
        "tag": "Серебро 925",
    },
    {
        "id": 3,
        "title": "Цепь «Raw Link»",
        "category": "Колье",
        "price": "8 200 ₽",
        "tag": "Черненое серебро",
    },
    {
        "id": 4,
        "title": "Браслет «Structure»",
        "category": "Браслеты",
        "price": "6 900 ₽",
        "tag": "Серебро 925",
    },
]


@app.route("/")
def index():
    return render_template("index.html", products=PRODUCTS)


if __name__ == "__main__":
    app.run(debug=True)