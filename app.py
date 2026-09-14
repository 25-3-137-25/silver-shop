from flask import Flask, render_template, request

app = Flask(__name__)

products = [
    {
        "id": 1,
        "title": "Кольцо Liquid Silver",
        "category": "Кольца",
        "price": "5 400 ₽",
        "tag": "Серебро 925",
        "image": "liqring.jpg",
        "description": "Кольцо из серебра 925 пробы. Можно посмотреть вживую при визите.",
    },
    {
        "id": 2,
        "title": "Кафф Minimal Edge",
        "category": "Серьги",
        "price": "3 800 ₽",
        "tag": "Серебро 925",
        "image": "kaff.jpg",
        "description": "Кафф без лишних деталей. Подходит для повседневного образа.",
    },
    {
        "id": 3,
        "title": "Цепь Raw Link",
        "category": "Цепи",
        "price": "8 200 ₽",
        "tag": "Черненое серебро",
        "image": "cep.jpg",
        "description": "Цепь из черненого серебра. Фактура лучше видна вживую.",
    },
]


@app.route("/")
def index():
    return render_template("index.html", products=products)


@app.route("/catalog")
def catalog():
    cat = request.args.get("cat")
    items = products
    if cat:
        items = [p for p in products if p["category"] == cat]
    return render_template("catalog.html", products=items, cat=cat)


@app.route("/item/<int:item_id>")
def item(item_id):
    product = None
    for p in products:
        if p["id"] == item_id:
            product = p
            break
    return render_template("item.html", product=product)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/form", methods=["GET", "POST"])
def form():
    error = ""
    result = None

    if request.method == "POST":
        name = request.form.get("name", "").strip()
        phone = request.form.get("phone", "").strip()
        comment = request.form.get("comment", "").strip()
        item_id = request.form.get("item_id", "")

        if name == "" or phone == "":
            error = "Нужно указать имя и телефон."
        elif len(phone) < 6:
            error = "Телефон слишком короткий."
        else:
            chosen = "не выбрано"
            for p in products:
                if str(p["id"]) == item_id:
                    chosen = p["title"]
                    break
            result = {
                "name": name,
                "phone": phone,
                "comment": comment,
                "item": chosen,
            }

    return render_template(
        "form.html",
        products=products,
        error=error,
        result=result,
    )


if __name__ == "__main__":
    app.run(debug=True)
