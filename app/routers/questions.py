from flask import Blueprint, jsonify, request
from pydantic import ValidationError

from app.models import Question, db
from app.schemas.question import QuestionCreate, QuestionResponse

questions_bp = Blueprint("questions", __name__)


@questions_bp.route('/', methods=['GET'])
def get_questions():
    """Retrieve a list of all questions."""
    questions = Question.query.all()
    results = [
        QuestionResponse.model_validate(question, from_attributes=True).model_dump()
        for question in questions
    ]
    return jsonify(results), 200


@questions_bp.route('/', methods=['POST'])
def create_question():
    """Create a new question with Pydantic validation."""
    data = request.get_json()

    try:
        question_data = QuestionCreate(**data)
    except ValidationError as e:
        return jsonify(e.errors()), 400

    new_question = Question(text=question_data.text)
    db.session.add(new_question)
    db.session.commit()

    return jsonify(QuestionResponse(
        id=new_question.id,
        text=new_question.text
    ).model_dump()), 201


@questions_bp.route("/<int:id>", methods=["GET"])
def get_question(id):
    """Retrieve details of a specific question by its ID."""
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
