# Step 1: Read the files
questions = []
answers = []

with open('questions.txt', 'r') as file:
    for line in file:
        questionNo, question = line.rsplit('.')  # Split questionNo and question
        questions.append(( int(questionNo), question.strip()))

with open('answer.txt', 'r') as file:
    for line in file:
        answerNo, answer = line.rsplit('.')  # Split answerNo and answer
        answers.append(( int(answerNo), answer.strip()))

# print(questions)
# Step 2: Sort both lists by numeric value
questions.sort(key=lambda x: x[0])
answers.sort(key=lambda x: x[0])

# Step 3: Create matched questionNo-answer pairs
with open('matched_output.txt', 'w') as output_file:
    for questionNo, question in questions:
        for answerNo, answer in answers:
            if questionNo == answerNo:
                output_file.write(f"{questionNo}. {question}\n{answer}\n")
                break
