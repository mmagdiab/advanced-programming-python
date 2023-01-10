"""
Your Program will read a list of questions,
a list of the corresponding correct answers, in addition to a list of wrong answers.
The program will then compose an MCQ exam paper of 5 random questions.
Each question in the exam paper will be associated with 4 choices. One of the choices will be its correct answer,
while the other choices will be wrong answer.
Your program will also read student responses and will grade them.
Each correct answer will count one mark and each wrong answer will count zero marks.
You are kindly required to write Python code to realize this idea.
The program is supposed to read response of 100 students and produce the exam results.
"""
from random import sample, shuffle

# MCQ creation
questions_bank = eval(input('Enter questions list:'))
answers_bank = eval(input('Enter corresponding answers list:'))
wrong_bank = eval(input('Enter wrong choices list:'))

random_question = sample(questions_bank, 5)  # Or get random 5 indexes -> sample(range(len(question_bank)), 5)

mcq_exam = [{  # each question -> {'question': value, 'answer': value, 'choices': value}
    'question': question,
    'answer': answers_bank[questions_bank.index(question)],
    'choices': sample(wrong_bank, 3) + [answers_bank[questions_bank.index(question)]]
} for question in random_question]

# student questioning
for i in range(100):
    student_score = 0
    shuffle(mcq_exam)
    for mcq in mcq_exam:
        print('Question: ' + mcq['question'])
        shuffle(mcq['choices'])
        print('Choices: ' + " - ".join(mcq['choices']))
        answer = input('Enter your answer:')
        if answer.lower() == mcq['answer'].lower():
            student_score += 1
    print(student_score)
