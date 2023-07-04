from ast import Global
from re import S
from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)


data = {}
current_p = 0

sales = [
    {
        "id": 1,
        "salesperson": "James D. Halpert",
        "client": "Shake Shack",
        "reams": 1000
    },
    {
        "id": 2,
        "salesperson": "Stanley Hudson",
        "client": "Toast",
        "reams": 4000
    },
    {
        "id": 3,
        "salesperson": "Michael G. Scott",
        "client": "Computer Science Department",
        "reams": 10000
    }
]
clients = [
    "Shake Shack",
    "Toast",
    "Computer Science Department",
    "Teacher's College",
    "Starbucks",
    "Subsconsious",
    "Flat Top",
    "Joe's Coffee",
    "Max Caffe",
    "Nussbaum & Wu",
    "Taco Bell",
]

# ROUTES
lessons = {
    "1": {
        "prev_lesson": "0",
        "lesson_id": "1",
        "title": "Introduction:",
        "text": "In Chinese zodiac there was <b>12 animals</b> stands for a year in a <b>12-year</b> cycle.",
        "pic": "circle1.png",
        "next_lesson": "2",
    },
    "2": {
        "prev_lesson": "1",
        "lesson_id": "2",
        "title": "Trick:",
        "text": "Let’s remember <b>2020 is year of RAT</b> <br>"
                "If you keep <b>adding or subtracting 12 from 2020</b>, <br>all the years you get belongs to this zodiac sign.",
        "pic": "timeline.png",
        "next_lesson": "3",},
    "3": {
        "prev_lesson": "2",
        "lesson_id": "3",
        "title": "Trick to remember the order:",
        "text": " <b>RAT</b> riding <b>OX</b> chased by <b>TIGER</b> with a <b>RABBIT</b> hat",

        "pic": "four1.PNG",
        "next_lesson": "4",
    },
    "4": {
        "prev_lesson": "3",
        "lesson_id": "4",
        "title": "Trick to remember the order:",
        "text": "<b>DRAGON</b> surpasses <b>SNAKE</b>, tailing by <b>HORSE</b> who ditched the angry <b>GOAT</b>",
        # Dragon surpasses Snake, tailing by Horse who ditched the angry Goat
        "pic": "four2.PNG",
        "next_lesson": "5",
    },
    "5": {
        "prev_lesson": "4",
        "lesson_id": "5",
        "title": "Trick to remember the order:",
        "text": "<b>MONKEY</b> tricks <b>ROOSTER</b> followed by <b>DOG</b> dragging a sleepy <b>PIG</b>",
        # Monkey tricks Rooster followed by Dog dragging a sleepy Pig
        "pic": "four3.PNG",
        "next_lesson": "6",
    },
    "6": {
        "prev_lesson": "5",
        "lesson_id": "6",
        "title": "Learn to find out the Zodiac at cerntain year:",
        "text": "A person born in 1999 has a zodiac sign of _____?",
        # Monkey tricks Rooster followed by Dog dragging a sleepy Pig
        "pic": "example.PNG",
        "next_lesson": "7",
    },
    "7": {
        "prev_lesson": "6",
        "lesson_id": "7",
        "next_lesson": "8",
    },

    "8": {
        "prev_lesson": "7",
        "lesson_id": "8",
        "title": "Congratulations on finish the reading!",
        "text": "Below is how you feel about previous pages, are you ready for the quiz?",
        "pic": "Congratulations.PNG",
        "next_lesson": "end",
    },

}

quizzes = {
    "1": {
        "prev_quiz": "0",
        "quiz_id": "1",
        "title": "Quiz 1:",
        "text": "How many Chinese Zodiac Signs are there?",
        "question": {"a": "12", "b": "24", "c": "10", "d": "60"},
        "pic": "circle1.png",
        "next_quiz": "2",
        "ans": 0,
        "selected": -1
    },
    "2":
        {
        "prev_quiz": "1",
        "quiz_id": "2",
        "title": "Quiz 2:",
        "text": "Is wolf one of the Chinese zodiac?",
        "question": {"a": "No", "b": "YES", "c": "Maybe", "d": "Not Sure"},
        "pic": "timeline.png",
        "next_quiz": "3",
        "ans": 0,
        "selected": -1
    },
    "3":
        {
        "prev_quiz": "2",
        "quiz_id": "3",
        "title": "Quiz 3:",
        "text": "Is cat one of the Chinese zodiac?",
        "question": {"a": "No", "b": "YES", "c": "Maybe", "d": "Not Sure"},
        "pic": "timeline.png",
        "next_quiz": "4",
        "ans": 0,
        "selected": -1
    },
    "4":
        {
        "prev_quiz": "3",
        "quiz_id": "4",
        "title": "Quiz 4:",
        "text": "Which one of the following is Chinese Zodiac?",
        "question": {"a": "Elephant", "b": "Cat", "c": "Leopard", "d": "Monkey"},
        "pic": "timeline.png",
        "next_quiz": "5",
        "ans": 3,
        "selected": -1
    },
    "5":
        {
        "prev_quiz": "4",
        "quiz_id": "5",
        "title": "Quiz 5:",
        "text": "A person born in 2020 has a zodiac sign of?",
        "question": {"a": "Dog", "b": "Cat", "c": "Rat", "d": "Monkey"},
        "pic": "timeline.png",
        "next_quiz": "6",
        "ans": 2,
        "selected": -1
    },
    "6":
        {
        "prev_quiz": "5",
        "quiz_id": "6",
        "title": "Quiz 6:",
        "text": "12 years before 2020, person born in 2008 has a zodiac sign of?",
        "question": {"a": "Dog", "b": "Cat", "c": "Rat", "d": "Monkey"},
        "pic": "timeline.png",
        "next_quiz": "7",
        "ans": 2,
        "selected": -1
    },
    "7":
        {
        "prev_quiz": "6",
        "quiz_id": "7",
        "title": "Quiz 7:",
        "text": "12 years before 2008, a person born in 1996 has a zodiac sign of?",
        "question": {"a": "Dog", "b": "Cat", "c": "Rat", "d": "Monkey"},
        "pic": "timeline.png",
        "next_quiz": "8",
        "ans": 2,
        "selected": -1
    },
    "8":
        {
        "prev_quiz": "7",
        "quiz_id": "8",
        "title": "Quiz 8:",
        "text": "2 years after rat, a person born in 1997 has a zodiac sign of?",
        "question": {"a": "Dog", "b": "Cat", "c": "Ox", "d": "Monkey"},
        "pic": "timeline.png",
        "next_quiz": "end",
        "ans": 2,
        "selected": -1
    }
}

quizzes_original = dict(quizzes)  # keep a copy of the orginal

# some helper functions


def calculate_score():
    result = []
    score = 0
    wrong = ""
    text = []
    sels = []
    for key, val in quizzes.items():
        if val["ans"] == val["selected"]:
            score += 1
            # print(val["selected"])
        else:
            wrong += key + ', '
            sel = val["selected"]
            if sel == 0:
                sel = val["question"]['a']
            elif sel == 1:
                sel = val["question"]['b']
            elif sel == 2:
                sel = val["question"]['c']
            elif sel == 3:
                sel = val["question"]['d']
            else:
                sel = 'empty'
            text.append(val["text"])
            sels.append(sel)
    result.append(wrong[:-2])
    result.append(score)
    result.append(text)
    result.append(sels)
    return result


def reset_quiz():
    global quizzes
    quizzes = dict(quizzes_original)


@ app.route('/learn/<lesson_id>')
def learn(lesson_id=0):
    # print(lessons["1"])
    lesson = lessons[lesson_id]
    return render_template('learn.html', lesson=lesson)


@ app.route('/quiz/<quiz_id>')
def quiz(quiz_id=0):
    # print(quiz["1"])
    quiz = quizzes[quiz_id]
    return render_template('quiz.html', quiz=quiz)


@ app.route('/quiz/end')
def quiz_end(result=[]):
    """
        calcualte score and reset quiz
    """
    global quizzes
    result = calculate_score()

    print("score: ", result[1])
    reset_quiz()
    if result[1] == 8:
        return render_template('quiz_end.html', result = result[1])

    else:
        return render_template('keep_trying.html', result = result)




@app.route('/learn/add_name', methods=['POST'])
def add_name():
    global data
    # global current_p

    json_data = request.get_json()
    name = json_data["name"]

    first =int( name[0])
    # print("first: "+first)
    data[first] = name
    if(first==7):
        del data[first]
    # data.update({first: name})

    return jsonify(data=data)


@app.route('/')
def home():
    return render_template('welcome.html')


@app.route('/learn/i6')
def learn_p():
    return render_template('learn_personality.html', lesson=lessons)


@app.route('/learn/n7')
def learn_p1():
    return render_template('index.html', lesson=lessons)


@app.route('/quiz/<item_id>', methods=["POST"])
def edit_item(item_id=None):
    json_data = request.get_json()
    json_data["id"] = str(item_id)
    # burger_data[str(item_id)] = json_data


    # 这里给页面参数，html加个地方传参数给js
    return jsonify(data={})

# AJAX FUNCTIONS


@app.route('/update', methods=['GET', 'POST'])
def update():
    item = request.get_json()
    quizzes[item["quiz_id"]] = item
    # print("info:", item, quizzes[item["quiz_id"]])
    return jsonify(0)


if __name__ == '__main__':
    app.run(debug=True)
