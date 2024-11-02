from app.models import Categories, Products


def load_categoris():
    return Categories.query.order_by("id").all()


def load_products(categoty_id=None, kw=None):
    query = Products.query

    if categoty_id:
        query = query.filter(Products.category_id == categoty_id)

    if kw:
        query = query.filter(Products.name.contains(kw))

    return query.all()
