import os
from unicodedata import category
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10


def paginate_question(request, selection):
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE
    #questions = [question.format() for question in selection]
    questions = []
    for question in selection :     
        questions.append({"id": question.id, "question":question.question, "answer":question.answer, "category": question.category, "dificulty":question.difficulty})

    
    return questions[start:end]



def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)

    """
     @TODO Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
    """
    cors = CORS(app, resources={r"*": {"origins": "*"}})

    """
    @TODO: Use the after_request decorator to set Access-Control-Allow
    """
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PATCH,POST,DELETE,OPTIONS')
        return response
    """
    @TODO:
    Create an endpoint to handle GET requests
    for all available categories.
    """
    @app.route('/categories', methods=['GET'])
    def categories():
        categories = Category.query.all()
        category_list = {}


        for categorie in categories:
                category_list[categorie.id] = categorie.type
        return jsonify({'category':category_list})

    """
    @TODO:
    Create an endpoint to handle GET requests for questions,
    including pagination (every 10 questions).
    This endpoint should return a list of questions,
    number of total questions, current category, categories.


    TEST: At this point, when you start the application
    you should see questions and categories generated,
    ten questions per page and pagination at the bottom of the screen for three pages.
    Clicking on the page numbers should update the questions.
    """
    @app.route('/questions', methods=['GET'])
    def question():
        selection = Question.query.all()
        nb_categories = Category.query.count()
        nb_questions = Question.query.count()
        categories = Category.query.all()
        categors =  [categorie.format() for categorie in categories]
        data_category = {}
        for categori in categories:
            data_category[categori.id]=categori.type

        questions = paginate_question(request, selection)
        
        return jsonify({'success': True, 'questions': questions, "categories": data_category, "totalQuestions": nb_questions, "current_category": 1})
    
    """
    
    @TODO:
    Create an endpoint to DELETE question using a question ID.

    TEST: When you click the trash icon next to a question, the question will be removed.
    This removal will persist in the database and when you refresh the page.
    """
    @app.route('/questions/<id>', methods=['DELETE'])
    def delete_question(id):
        identifiant = id
       
        data = Question.query.filter_by(id=identifiant).first()
        data.delete()
   
        return jsonify({"id": id})
       
    """
    @TODO:
    Create an endpoint to POST a new question,
    which will require the question and answer text,
    category, and difficulty score.

    TEST: When you submit a question on the "Add" tab,
    the form will clear and the question will appear at the end of the last page
    of the questions list in the "List" tab.
    """
    @app.route('/questions', methods=['POST'])
    def post_question():
        # rquestion = request.args.get('question', None)
        #return jsonify({"data":"ok"})
        rquestion = request.get_json()['question']
        
        r_answer = request.get_json()['answer']
        
        category_id = request.get_json()['category']
        
        difficulty = request.get_json()['difficulty']
       
        question = Question(question= rquestion, answer = r_answer, category= category_id, difficulty=difficulty)
        question.insert()
        return jsonify({"question": question.format()})
        

    """
    @TODO:
    Create a POST endpoint to get questions based on a search term.
    It should return any questions for whom the search term
    is a substring of the question.

    TEST: Search by any phrase. The questions list will update to include
    only question that include that string within their question.
    Try using the word "title" to start.
    """
    @app.route('/questions/search/', methods=['POST'])
    def search_question():
            
            rquestion = request.get_json()['searchTerm']
           # return jsonify({"data": "donnees"})
            selection = Question.query.filter(Question.question.ilike(f'%{rquestion}%')).all()
            
            data = []
            catego=""
            for question in selection :
                catego = Category.query.filter_by(id=question.category).first().type if Category.query.filter_by(id=question.category).first() else None
                data.append({"id": question.id, "question":question.question, "category": question.category, "dificulty":question.difficulty, "answer":question.answer})
            selection = data
            
            return jsonify({"questions": selection, "totalQuestions": len(data), "current_category": catego})

    """
    @TODO:
    Create a GET endpoint to get questions based on category.

    TEST: In the "List" tab / main screen, clicking on one of the
    categories in the left column will cause only questions of that
    category to be shown.
    """
    @app.route('/category/<categori>/questions', methods=['GET'])
    def get_categorie_question(categori):
        questions = Question.query.filter_by(category = categori).all()
        categorie = Category.query.filter_by(id = categori).first().format()
        data = []
        for question in questions :
            data.append(question.format())
        return jsonify({"questions": data, "currentCategory": categorie["type"], "total_questions": len(data)})
    """
    @TODO:
    Create a POST endpoint to get questions to play the quiz.
    This endpoint should take category and previous question parameters
    and return a random questions within the given category,
    if provided, and that is not one of the previous questions.

    TEST: In the "Play" tab, after a user selects "All" or a category,
    one question at a time is displayed, the user is allowed to answer
    and shown whether they were correct or not.
    """
    @app.route('/quizzes', methods=['POST'])
    def playing():
        
        preview_question= request.get_json()['previous_questions']
        
        questions = Question.query.all()
        
        x = random.randint(0,len(questions)-1)
        data = []
        while(questions[x].id in preview_question):
            x = random.randint(0,len(questions)-1)
            
        return jsonify({"question": {"id": questions[x].id, "question":questions[x].question, "answer":questions[x].answer, "category": Category.query.filter_by(id=questions[x].category).first().type, "dificulty":questions[x].difficulty}})
    """
    @TODO:
    Create error handlers for all expected errors
    including 404 and 422.
    """
    @app.errorhandler(404)
    def not_found(error):
            return jsonify({
    "success": False,
    "error": 404,
    "message": "Not found"
}), 404

    @app.errorhandler(405)
    def not_found(error):
            return jsonify({
    "success": False,
    "error": 405,
    "message": "Method not allowed"
}), 405


    @app.errorhandler(422)
    def not_found(error):
            return jsonify({
    "success": False,
    "error": 422,
    "message": "unprocessable"
}), 422

    @app.errorhandler(403)
    def not_found(error):
            return jsonify({
    "success": False,
    "error": 403,
    "message": "Forbidden"
}), 403

   
    @app.errorhandler(500)
    def not_found(error):
            return jsonify({
    "success": False,
    "error": 500,
    "message": "internal server error"
}), 500
    return app

