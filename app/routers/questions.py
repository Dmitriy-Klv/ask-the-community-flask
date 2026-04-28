from flask import Blueprint, request

questions_bp = Blueprint('questions', __name__)

@questions_bp.route('/', methods=['GET'])
def get_questions():
    """Retrieve a list of all questions."""
    return "List of all questions"

@questions_bp.route('/', methods=['POST'])
def create_question():
    """Create a new question."""
    return "Question created"

@questions_bp.route('/<int:id>', methods=['GET'])
def get_question(id):
    """Retrieve details of a specific question by its ID."""
    return f"Details of question {id}"

@questions_bp.route('/<int:id>', methods=['PUT'])
def update_question(id):
    """Update a specific question by its ID."""
    return f"Question {id} updated"

@questions_bp.route('/<int:id>', methods=['DELETE'])
def delete_question(id):
    """Delete a specific question by its ID."""
    return f"Question {id} deleted"