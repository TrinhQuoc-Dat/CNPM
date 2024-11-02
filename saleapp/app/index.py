from flask import render_template, request
import dao
from app import app


@app.route("/")
def index():

    cates_id = request.args.get('category_id')
    kw = request.args.get('kw')
    cates = dao.load_categoris()
    prods = dao.load_products(categoty_id=cates_id, kw=kw)
    return render_template('index.html', categories= cates, products= prods)


if __name__ == '__main__':
    app.run(debug=True)
