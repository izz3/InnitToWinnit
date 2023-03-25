import sqlite3
import random
from flask import Flask, render_template, request

# Connect to the database
conn = sqlite3.connect('emo_track_responses.db')

# Create a cursor object
cursor = conn.cursor()

# Create a table
table_dont_exist = cursor.fetchone() is None 
if not table_dont_exist:
    cursor.execute('''CREATE TABLE emo_track_responses
                    (id INTEGER PRIMARY KEY, Answer TEXT, Responses TEXT)''')


# Insert some data into the table
bad_answers = ["It's okay z", 
               "You probably got this z", 
               "ove you z", 
               "fear is the mind-killer z", 
               "let go of your earthly tethers z",
               "when we hit our lowest point we are open to greatest change z", 
               "If you look for light you will find it. If you don't all you will see is darkness z", 
               "Don't rush to figure it all out. Let life suprise you"]
bad_str = ', '.join(bad_answers)


good_answers = ["You are doing an amazing job! Keep up the great work. z",
                "You should be proud of yourself for all that you've accomplished today. z",
                "You are making progress and moving forward. Keep going, you're doing great! z",
                "You're doing everything right! Keep it up and keep pushing forward. z",
                "You're really on a roll today! Keep up the momentum. z",
                "Your hard work and effort is paying off. You're doing great! z",
                "I can tell you're putting in a lot of effort and it's really paying off. Keep it up! z",
                "You are doing fantastic today. Keep up the good work and you will achieve great things. z",
                "It's clear that you're making great progress today. Keep up the momentum and you'll go far. z",
                "Your hard work and dedication to your tasks is truly admirable. Keep it up! z"]
good_str = ', '.join(good_answers)

mid_answers = ["nice"]
mid_str = ', '.join(mid_answers)

cursor.execute("INSERT INTO emo_track_responses (id, Answer, Responses) VALUES (?, ?, ?)", (0, "Bad", bad_str))
cursor.execute("INSERT INTO emo_track_responses (id, Answer, Responses) VALUES (?, ?, ?)", (1, "Good", good_str))
cursor.execute("INSERT INTO emo_track_responses (id, Answer, Responses) VALUES (?, ?, ?)", (2, "Neutral", mid_str))

def getResponses(UserInput):
    # Retrieve the list of strings from the Responses column
    cursor.execute("SELECT Responses FROM emo_track_responses WHERE Answer = ?", (UserInput,))
    responses_tuple = cursor.fetchone()
    if responses_tuple is not None:
        my_string = responses_tuple[0]
        responses_list = my_string.split(" z,")
        random_index = random.randint(0, len(responses_list) - 1)
        response_str = responses_list[random_index]
        print(response_str)  
        return response_str
    else:
        print("Sorry, I don't have a response for that.")


## Create a new instance of the Flask class
app = Flask(__name__)

## Define a route for submitting the form data
@app.route('/')
def form():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    user_input = request.form['user_input']
    response = api.getResponses(user_input)
    return render_template('response.html', display=response)

if __name__ == '__main__':
    app.run(debug=True)
