import os
import random

'''
Random Quiz Generator
 - creates a randomized quiz of US state capitals
 - 35 different quizzes, each with 50 multiple-choice questions in random order
 - provide the correct answer and three random wrong answers for each question
 - write the quizzes to 35 text files, write the answer keys to 35 text files

'''

# populate the dictionary of state capitals first
state_capitals = {}
for line in open('state_capitals.csv'):
    state, capital = line.strip().split(',')
    state_capitals[state] = capital

if not os.path.exists('quizzes'):
    os.mkdir('quizzes')

answer_letters = {0:'A', 1:'B', 2:'C', 3:'D'}

for quiz_num in range(1,36):
    quiz_name = 'quizzes/quiz-%d.txt' % quiz_num
    answer_name = 'quizzes/answer-%d.txt' % quiz_num
    with open(quiz_name, 'w') as quiz_file:
        with open(answer_name, 'w') as answer_file:
            states = list(state_capitals.keys())
            capitals = list(state_capitals.values())
            random.shuffle(states)
            quiz_file.write("Name:\n")
            quiz_file.write("Date:\n")
            quiz_file.write("Period:\n")
            quiz_file.write("\n\n\tState Capital Quiz (version %d)\n\n\n" % quiz_num)
            for i, state in enumerate(states):
                # pick three other answers
                answers = []
                answers.append(state_capitals[state])
                while len(answers) != 4:
                    choice = random.choice(capitals)
                    if choice not in answers:
                        answers.append(choice)
                random.shuffle(answers)
                answer_letter = answer_letters[answers.index(state_capitals[state])]
                quiz_file.write('%d. What is the capital of %s?\n\tA. %s\n\tB. %s\n\tC. %s\n\tD. %s\n\n' % (i+1, state, answers[0],
                                                                                               answers[1], answers[2], answers[3]))
                answer_file.write('%d. %s %s\n' % (i+1, answer_letter, state_capitals[state]))
