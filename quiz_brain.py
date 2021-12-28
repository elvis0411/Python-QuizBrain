from _typeshed import Self


class QuizBrain:
    def __init__(self,question_list):
        self.question_number = 0
        self.question_list = question_list 
        self.score = 0
        
    def next_question(self):
        current_qeustion = self.question_list[self.question_number]
        self.question_number += 1
        user_ans = input(f'Q.{self.question_number}: {current_qeustion.text} (True/False)?: ')
        self.check_answer(user_ans,current_qeustion.answer)

    def still_has_questions(self):
        total_number = len(self.question_list)
        current_number = self.question_number
        return current_number < total_number

    def check_answer(self,input_ans, correct_ans):
        if input_ans.lower() == correct_ans.lower():
            self.score +=1
            print("You got it Correct")
        else:
            print("That's wrong")
        print(f"The correct answer is {correct_ans}.")
        print(f"Your current score is: {self.score}/{self.question_number}.")
        print("\n")




        
