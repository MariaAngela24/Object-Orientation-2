class Student(object):
    """Any Student"""


    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address


class Question(object):
    """Any question and correct answer"""


    def __init__(self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer
        

class Exam(object):
    """Any Exam"""
    
    def __init__(self, name):
        questions = []
        self.name = name
    

    