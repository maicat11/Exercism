def calculate(question):
    question = question.strip('What is').strip('?').replace('by ', '')

    operators = [('plus', '+'), ('minus', '-'), ('multiplied', '*'), ('divided', '//')]

    for word, operator in operators:
        question = question.replace(word, operator)

    question = question.split()

    try:
        while len(question) > 1:
            first_num = eval(' '.join(question[:3]))
            question = [str(first_num)] + question[3:]
        return int(question[0])
    except (NameError, SyntaxError, IndexError):
        raise ValueError('Not a valid math problem.')