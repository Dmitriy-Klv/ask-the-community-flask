from flask import Blueprint, request

response_bp = Blueprint('response', __name__)

@response_bp.route('/', methods=['GET'])
def get_responses():
    """
    Retrieve statistics for all responses.
    """
    return "Statistics for all responses"

@response_bp.route('/', methods=['POST'])
def add_response():
    """
    Add a new response (vote) to a specific question.
    """
    return "Response added successfully"