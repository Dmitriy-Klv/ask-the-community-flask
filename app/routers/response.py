from flask import Blueprint, jsonify, request

from app.models import Question, Response, Statistic, db

response_bp = Blueprint("response", __name__, url_prefix="/responses")


@response_bp.route("/", methods=["GET"])
def get_responses():
    """Retrieve aggregated response statistics."""
    statistics = Statistic.query.all()
    results = [
        {
            "question_id": stat.question_id,
            "agree_count": stat.agree_count,
            "disagree_count": stat.disagree_count,
        }
        for stat in statistics
    ]

    return jsonify(results), 200


@response_bp.route("/", methods=["POST"])
def add_response():
    """Add a new response to a question and update statistics."""

    data = request.get_json()

    if not data or "question_id" not in data or "is_agree" not in data:
        return jsonify({"error": "Invalid data provided"}), 400

    question = Question.query.get(data["question_id"])
    if not question:
        return jsonify({"error": "Question not found"}), 404

    new_response = Response(question_id=question.id, is_agree=data["is_agree"])
    db.session.add(new_response)

    statistic = Statistic.query.filter_by(question_id=question.id).first()
    if not statistic:
        statistic = Statistic(question_id=question.id, agree_count=0, disagree_count=0)
        db.session.add(statistic)

    if data["is_agree"]:
        statistic.agree_count += 1
    else:
        statistic.disagree_count += 1

    try:
        db.session.commit()
        return (
            jsonify(
                {
                    "message": f"Response to question {question.id} added successfully",
                    "question_id": question.id,
                }
            ),
            201,
        )
    except Exception:
        db.session.rollback()
        return jsonify({"error": "Database transaction failed"}), 500
