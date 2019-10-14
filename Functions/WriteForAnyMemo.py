

def write(list_questions, list_answers):
    with open('file.txt', 'w', encoding='utf-8') as f:
        for question, answer in zip(list_questions, list_answers):
            if question != '--------':
                f.write(question + '\t'+answer + '\n')




