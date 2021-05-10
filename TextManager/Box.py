class Box:

    id = 'placeholder'
    description = 'placeholder'
    answers = []

    def __init__(self, raw_dict):
        print("Creating " + raw_dict['id'] + " box")
        self.id = raw_dict['id']
        print(self.id)
        self.description = raw_dict['description']
        print(self.description)
        for x in raw_dict['answers']['answer']:
            print(x)
            new_answer = Answer(x.get('text'), x.get('goto'))
            # self.answers['text'] = x.get('text')
            # self.answers['goto'] = x.get('goto')
            self.answers.append(new_answer)


class Answer:

    text = 'default text'
    goto = 'default goto'

    def __init__(self, text, goto):
        self.text = text
        self.goto = goto
