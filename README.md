

***GET '/categories' :

Retrieves a dictionary of categories in which the keys are the IDs, and the value is the corresponding category string
Query arguments: none
Returns: object with a single key, 'categories', which contains an object of id:category_string key:value pairs.
{
"category": {
"1": "Science",
"2": "Art",
"3": "Geography",
"4": "History",
"5": "Entertainment",
"6": "Sports"
}
}

***GET '/questions' : 
retrieves a dictionary containing questions with their categories, as well as the total number of questions.
Query arguments: none
keys:
- question: list of questions,
- totalQuestions: total number of questions
-categories: list of categories

{
"Questions": [
{
"category": 4,
"dificulty": 1,
"id": 9,
"question": "What boxer's original name is Cassius Clay?"
},
{
"category": 5,
"dificulty": 4,
"id": 2,
"question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
},
{
"category": 5,
"dificulty": 4,
"id": 4,
"question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
},
{
"category": 5,
"dificulty": 3,
"id": 6,
"question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
},
{
"category": 6,
"dificulty": 3,
"id": 10,
"question": "Which is the only team to play in every soccer World Cup tournament?"
},
{
"category": 6,
"dificulty": 4,
"id": 11,
"question": "Which country won the first ever soccer World Cup in 1930?"
},
{
"category": 4,
"dificulty": 2,
"id": 12,
"question": "Who invented Peanut Butter?"
},
{
"category": 3,
"dificulty": 2,
"id": 13,
"question": "What is the largest lake in Africa?"
},
{
"category": 3,
"dificulty": 3,
"id": 14,
"question": "In which royal palace would you find the Hall of Mirrors?"
},
{
"category": 3,
"dificulty": 2,
"id": 15,
"question": "The Taj Mahal is located in which Indian city?"
}
],
"categories": [
{
"id": 1,
"type": "Science"
},
{
"id": 2,
"type": "Art"
},
{
"id": 3,
"type": "Geography"
},
{
"id": 4,
"type": "History"
},
{
"id": 5,
"type": "Entertainment"
},
{
"id": 6,
"type": "Sports"
}
],
"success": true,
"totalQuestions": 19
}

DELETE '/questions/<id>': 
delete a question following an id sent in the request header
and returns the question id in a dictionary
Query arguments: id of question

{
    'id': 4
}

***POST '/questions':
adds a new question in the database,
the required arguments in JSON format are:
- question: character string containing the question,
- answer: character string containing the answer,
- difficulty: integer to specify the level of difficulty
- category: integer containing the id of the category to which your question is attached
return value: the question after insertion into the database
{
   "question":         {
"category": "Geography",
"dificulty": 3,
"id": 14,
"question": "In which royal palace would you find the Hall of Mirrors?"
}
}





***POST '/questions/search/'

returns the questions matching your search
the search term must be sent via the search_term key
Query arguments: search_term  

{
"Questions": [
{
"category": "History",
"dificulty": 1,
"id": 9,
"question": "What boxer's original name is Cassius Clay?"
}
],

"success": true
}

***GET '/category/<categori>/questions/'

returns the list of questions in the category specified in the header
required arguments: the category id

{
"currentCategory": "Art",
"question": [
{
"answer": "Escher",
"category": 2,
"difficulty": 1,
"id": 16,
"question": "Which Dutch graphic artist–initials M C was a creator of optical illusions?"
},
{
"answer": "Mona Lisa",
"category": 2,
"difficulty": 3,
"id": 17,
"question": "La Giaconda is better known as what?"
},
{
"answer": "One",
"category": 2,
"difficulty": 4,
"id": 18,
"question": "How many paintings did Van Gogh sell in his lifetime?"
},
{
"answer": "Jackson Pollock",
"category": 2,
"difficulty": 2,
"id": 19,
"question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
}
],
"totalQuestions": 4
}

*** POST '/play'

returns a random question different from the question whose id was sent in the request