# -*- coding: utf-8 -*-
"""
@title: Capstone Project

@author: BSlat
"""
import datetime;
import sys

class student():
    
    def __init__(self, first, last, student_id):
        self.first_name = first
        self.last_name = last
        self.student_id = student_id
        self.q_array = []

class question():
    
    def __init__(self, num):
        
        self.question_num = num
        self.question = ""
        self.correct_answer = ""
        self.time_limit = 0.00
        
        self.time_start = 0    
        self.time_stop = 0
        self.time_diff = 0
        self.student_answer = ""
        self.cheat_flag = False
        
    def toString(self):
        print("The student answered: ", self.student_answer, " in ", self.time_diff, " seconds.")
  
def takeQuiz(student, quiz):
    for num in range(len(quiz)):
        student.q_array.insert(num, question(num + 1))
        student.q_array[num].question = quiz[num].question
        student.q_array[num].correct_answer = quiz[num].correct_answer
        student.q_array[num].time_limit = quiz[num].time_limit
        
        student.q_array[num].time_start = datetime.datetime.today()
        student.q_array[num].student_answer = input(quiz[num].question)
        student.q_array[num].time_stop = datetime.datetime.today()
      
                
        delta = student.q_array[num].time_stop - student.q_array[num].time_start
        student.q_array[num].time_diff = delta.total_seconds()
        
        if((student.q_array[num].time_diff <= student.q_array[num].time_limit) and 
           (student.q_array[num].student_answer.lower() == student.q_array[num].correct_answer.lower())):
            
            student.q_array[num].cheat_flag = True
        
        student.q_array[num].toString()
 
def fileReport(student_array):
    
    for s in student_array:
        print("\nThis is the report for", s.first_name, s.last_name, "student id number:", s.student_id)
        num_flags = 0
        
        for q in s.q_array:
            if q.cheat_flag:
                print("The student was flagged for cheating on question: ", q.question_num)
                num_flags += 1
        
        print("Number of flagged questions: ", num_flags, "out of", len(s.q_array))
            
def makeQuiz():
    try:
        file = open("questions.txt", "r")
    except:
        print("Could not open question text file!")
        sys.exit
    
    num_questions = int(file.readline())
    q_array = []
    
    for num in range(num_questions):
        q_array.insert(num, question(num + 1))
        
        q_array[num].question = file.readline()
        q_array[num].question += file.readline()
        q_array[num].question += file.readline()
        q_array[num].question += file.readline()
        q_array[num].question += file.readline()
                
        char = file.readline()
        q_array[num].correct_answer = char[0]
        
        q_array[num].time_limit = float(file.readline())
    
    file.close()
    
    return q_array
 
def startProcess(student_array, quiz):
    count = 0
    
    while True:
        while True:
            try:
                name = input("Enter student's full name (First Last): ")
            
                first, last = name.split(" ")
                break
            except:
                print("Invalid name!\n")
                
        while True:
            id_number = input("\nEnter student's four digit student ID: ")
        
            if len(id_number) == 4: 
                break
            else:
                print("Invalid id number!")
                
        student_array.append(student(first, last, id_number))
        
        print("\n---The quiz will begin now---\n")
        
        takeQuiz(student_array[count], quiz)
        
        flag = input("Is there another student taking the test? ")
        
        if flag == 0 or flag.lower() == "no" or flag.lower() == "n":
            break
        else: 
            count += 1
       
if __name__ == '__main__':

    quiz = makeQuiz()
    student_array = []      

    startProcess(student_array, quiz)
    fileReport(student_array)