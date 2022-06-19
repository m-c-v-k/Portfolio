#! python3
# random_quiz_generator.py
# Creates quizzes with questions and answers in random order, along with the answer key.

import random
import os

capitals = {
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona': 'Phoenix',
    'Arkansas': 'Little Rock',
    'California': 'Sacramento',
    'Colorando': 'Denver',
    'Conneticut': 'Hartford',
    'Delaware': 'Dover',
    'Florida': 'Tallahassee',
    'Georgia': 'Atlanta',
    'Hawaii': 'Honolulu',
    'Idaho': 'Boise',
    'Illinois': 'Springfield',
    'Indiana': 'Indianapolis',
    'Iowa': 'Des Moines',
    'Kansas': 'Topeka',
    'Kentucky': 'Frankfort',
    'Louisiana': 'Baton Rouge',
    'Maine': 'Augusta',
    'Maryland': 'Annapolis',
    'Massachusatts': 'Boston',
    'Michigan': 'Lansing',
    'Minnesota': 'Saint Paul',
    'Mississippi': 'Jackson',
    'Missouri': 'Jefferson City',
    'Montana': 'Helena',
    'Nebraska': 'Lincoln',
    'Nevada': 'Carson City',
    'New Hampshire': 'Concord',
    'New Jersey': 'Trenton',
    'New Mexico': 'Santa Fe',
    'New York': 'Albany',
    'North Carolina': 'Raleigh',
    'North Dakota': 'Bismarck',
    'Ohio': 'Columbus',
    'Oklahoma': 'Oklahoma City',
    'Oregon': 'Salem',
    'Pennsylvania': 'Harrisburg',
    'Rhode Island': 'Providence',
    'South Carolina': 'Columbia',
    'South Dakota': 'Pierre',
    'Tennessee': 'Nashville',
    'Texas': 'Austin',
    'Utah': 'Salt Lake City',
    'Vermont': 'Montpelier',
    'Virginia': 'Richmond',
    'Washington': 'Olympia',
    'West Virginia': 'Charleston',
    'Wisconsin': 'Madison',
    'Wyoming': 'Cheyenne'
}


def generate_quiz(inp_dict, ammount):
    ''' generate_quiz generates a randomized quiz with unique sheets for each participant.

    Args:
        inp_dict (Dictionary): A dictionary containing the keyword and it's associated answer.
        ammout (Int): The number of quizes to be made

    Returns:
        None: Returns None
    '''

    for quiz_num in range(ammount):

        # Generates range quiz files
        quiz_file = open(str(os.getcwd(
        )) + str(os.path.join('\\Python', 'Automate_the_Boring_stuff_with_Python',
                              'support_files', 'quiz', 'capitals_quiz%s.txt' % (quiz_num + 1))), 'w+')
        answer_key_file = open(str(os.getcwd(
        )) + str(os.path.join('\\Python', 'Automate_the_Boring_stuff_with_Python',
                              'support_files', 'quiz', 'capitals_quiz_key%s.txt' % (quiz_num + 1))), 'w+')

        quiz_file.write('Name:\n\nDare:\n\nPeriod:\n\n')
        quiz_file.write((' ' * 20) + 'State Capitals Quiz (Form %s)' %
                        (quiz_num + 1))
        quiz_file.write('\n\n')

        states = list(inp_dict.keys())
        random.shuffle(states)

        # Loop through all 50 states, making a question for each.
        for question_num in range(50):
            correct_answer = inp_dict[states[question_num]]
            wrong_answers = list(inp_dict.values())
            del wrong_answers[wrong_answers.index(correct_answer)]
            wrong_answers = random.sample(wrong_answers, 3)
            answer_options = wrong_answers + [correct_answer]
            random.shuffle(answer_options)

            # Write the question and the answer to the quiz files.
            quiz_file.write('%s. What is the capital of %s\n' %
                            (question_num + 1, states[question_num]))

            for i in range(4):
                quiz_file.write('    %s. %s\n' %
                                ('ABCD'[i], answer_options[i]))

            quiz_file.write('\n')

            # Write the answer key to a file
            answer_key_file.write('%s. %s\n' % (
                question_num + 1, 'ABCD'[answer_options.index(correct_answer)]))

    quiz_file.close()
    answer_key_file.close()

    return None


generate_quiz(capitals, 35)
