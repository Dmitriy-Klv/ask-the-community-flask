from flask import Blueprint, jsonify, request
from pydantic import ValidationError

from app.models import Category, db
from app.schemas.category import CategoryCreate, CategoryResponse

category_bp = Blueprint("categories", __name__)


@category_bp.route('/', methods=['GET'])
def get_categories():
    """Retrieve a list of all get_categories."""
    categories = Category.query.all()
    results = [
        CategoryResponse.model_validate(category, from_attributes=True).model_dump()
        for category in categories
    ]
    return jsonify(results), 200


@category_bp.route('/', methods=['POST'])
def create_categories():
    """Create a new category with Pydantic validation."""
    data = request.get_json()

    try:
        categories_data = CategoryCreate(**data)
    except ValidationError as e:
        return jsonify(e.errors()), 400

    new_category = Category(name=categories_data.name)
    db.session.add(new_category)
    db.session.commit()

    return jsonify(CategoryResponse.model_validate(new_category).model_dump()), 201


@category_bp.route("/<int:id>", methods=["PUT"])
def update_categories(id):
    """Update a specific Categories by its ID."""
    category = Category.query.get(id)
    if category is None:
        return jsonify({"error": "Category not found"}), 404

    data = request.get_json()
    if not data or "name" not in data:
        return jsonify({"error": "No name provided for update"}), 400

    category.name = data["name"]
    db.session.commit()

    return (jsonify(
        {
            "message": "Category updated successfully",
                "id": category.id,
                "new_name": category.name,

        }
    ), 200
    )

@category_bp.route("/<int:id>", methods=["DELETE"])
def delete_category(id):
    """Delete a specific category by its ID."""
    category = Category.query.get(id)

    if category is None:
        return jsonify({"error: Category not found"}), 404

    db.session.delete(category)
    db.session.commit()

    return jsonify({"message": f"Category with id {id} has been deleted"}), 200





