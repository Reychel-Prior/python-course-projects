class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list

    def next_question(self):
        index = self.question_number
        q_text = self.question_list[index].text
        q_answer = self.question_list[index].answer

        user_answer = input(f"Q.{index + 1}: {q_text} (True/False)?: ")