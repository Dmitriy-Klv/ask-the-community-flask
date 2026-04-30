from flask import Blueprint, jsonify, request

from app.models import Question, db

questions_bp = Blueprint("questions", __name__)


@questions_bp.route("/", methods=["GET"])
def get_questions():
    """Retrieve a list of all questions."""
    questions = Question.query.all()
    questions_data = [{"id": q.id, "text": q.text} for q in questions]
    return jsonify(questions_data)


@questions_bp.route("/", methods=["POST"])
def create_question():
    """Create a new question."""
    data = request.get_json()
    if not data or "text" not in data:
        return jsonify({"error": "No question text provided"}), 400

    question = Question(text=data["text"])
    db.session.add(question)
    db.session.commit()

    return jsonify({"message": "Question created", "id": question.id}), 201


@questions_bp.route("/<int:id>", methods=["GET"])
def get_question(id):
    """
    Retrieve details of a specific question by its ID.
    """
    question = Question.query.get(id)

    if question is None:
        return jsonify({"error": "Question not found"}), 404

    return jsonify({"id": question.id, "text": question.text}), 200


@questions_bp.route("/<int:id>", methods=["PUT"])
def update_question(id):
    """
    Update a specific question by its ID.
    """
    question = Question.query.get(id)
    if question is None:
        return jsonify({"error": "Question not found"}), 404

    data = request.get_json()
    if not data or "text" not in data:
        return jsonify({"error": "No text provided for update"}), 400

    question.text = data["text"]
    db.session.commit()

    return (
        jsonify(
            {
                "message": "Question updated successfully",
                "id": question.id,
                "new_text": question.text,
            }
        ),
        200,
    )


@questions_bp.route("/<int:id>", methods=["DELETE"])
def delete_question(id):
    """
    Delete a specific question by its ID.
    """
    question = Question.query.get(id)

    if question is None:
        return jsonify({"error": "Question not found"}), 404

    db.session.delete(question)
    db.session.commit()

    return jsonify({"message": f"Question with ID {id} has been deleted"}), 200
