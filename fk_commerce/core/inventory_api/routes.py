from . import inventory_category_api_blueprint
from core.schema import CategorySchema
from apifairy import response, body
from core.models import Category
from flask import abort
from core import database as db


@inventory_category_api_blueprint.route(rule="/categories", methods=["GET"])
@response(CategorySchema(many=True))
def get_categories():
    return Category.query.all()


@inventory_category_api_blueprint.route(rule="/category", methods=["POST"])
@response(CategorySchema)
@body(CategorySchema)
# @other_responses({400: ""})
def create_category(data):

    if Category.query.filter(Category.name == data["name"]).first():
        abort(400, f"Category with name: {data['name']} exists")

    data["slug"] = data["name"].lower().replace(" ", "-").replace("_", "-")
    category = Category(
        **data,
    )
    db.session.add(category)
    db.session.commit()
    db.session.refresh(category)

    return category


@inventory_category_api_blueprint.route(rule="/category/<int:index>", methods=["GET"])
@response(CategorySchema)
# @other_responses({400: ""})
def get_category(index: int):

    category = Category.query.filter(Category.id == index).first()
    if category is None:

        abort(404, "Category not found")

    return category


@inventory_category_api_blueprint.route(
    rule="/category/<int:index>", methods=["DELETE"]
)
# @other_responses({400: ""})
def delete_category(index: int):

    category = Category.query.filter(Category.id == index).first()
    if category is None:

        abort(404, "Category not found")

    db.session.delete(category)
    db.session.commit()

    return {}
