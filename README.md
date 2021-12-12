# Capstone Project

# Description

This project is designed to facilitate in catching students cheating on quizzes/tests. The idea is to take the times a student starts and answeres a question and then finding the difference of those. If the student correctly answers a question extremely fast there are two possibilities, either they guessed and got lucky or they cheated and knew the answer. The time limits that the students are being compared to are predetermined by the faculty and instructors issuing the quizzes/tests to define a suitable minimum time. After the student has taken the quiz/test their results are then displayed to lay out which questions were flagged as being answered too fast, it is then up to the faculty/instructor to either retest or make the final decisions.

# Input

The input for the test should be given in a text file. Where the first line of the file is an integer value of how many questions are on the quiz/test. Following that should be the question and A-D multiple choice answers on separate lines. Then the correct answer should be given on its own line as either A, B, C, or D then the following line is the minimum time limit in seconds. A sample quiz is given within the questions.txt file, but can also be seen below:

    5
    What is 1 + 1?
    A) 0
    B) 1
    C) 2
    D) 3
    C
    1
    What is 1 - 1?
    A) 0
    B) 1
    C) 2
    D) 3
    A
    1
    What is 1 * 1?
    A) 0
    B) 1
    C) 2
    D) 3
    B
    1
    What is 1 / 1?
    A) 0
    B) 1
    C) 2
    D) 3
    B
    1
    What is 1 + 2?
    A) 0
    B) 1
    C) 2
    D) 3
    D
    1
    
 Aside from the quiz/test input the program will ask for the students first and last name along with a four digit (simulated) student ID number. Once all of the questions are answered another student will then be able to answer the same quiz/test.
 
# Output 

The project is designed to flag whether a student correctly answered a question too fast as determined by the faculty/instructor and then report the findings. At the end of the program a report will be given for each student and each question that was flagged, leading to a ratio of flagged questions to total questions. Going further all of this information will be visable via cloud/database format to the faculty/instructor for review. As well as possibly implementing facial recognition software to further flag cheating students through eye movements to notes or other sources of answers. The sample output can be found within the output.txt file and also as seen below:

    Enter student's full name (First Last): Bradley S


    Enter student's four digit student ID: 1111

    ---The quiz will begin now---


    What is 1 + 1?
    A) 0
    B) 1
    C) 2
    D) 3
    c
    The student answered:  c  in  3.59357  seconds.

    What is 1 - 1?
    A) 0
    B) 1
    C) 2
    D) 3
    a
    The student answered:  a  in  0.3281  seconds.

    What is 1 * 1?
    A) 0
    B) 1
    C) 2
    D) 3
    b
    The student answered:  b  in  0.281237  seconds.

    What is 1 / 1?
    A) 0
    B) 1
    C) 2
    D) 3
    b
    The student answered:  b  in  0.343651  seconds.

    What is 1 + 2?
    A) 0
    B) 1
    C) 2
    D) 3
    d
    The student answered:  d  in  0.32817  seconds.

    Is there another student taking the test? y

    Enter student's full name (First Last): brittany d


    Enter student's four digit student ID: 2222

    ---The quiz will begin now---


    What is 1 + 1?
    A) 0
    B) 1
    C) 2
    D) 3
    c
    The student answered:  c  in  2.453645  seconds.

    What is 1 - 1?
    A) 0
    B) 1
    C) 2
    D) 3
    a
    The student answered:  a  in  1.484273  seconds.

    What is 1 * 1?
    A) 0
    B) 1
    C) 2
    D) 3
    b
    The student answered:  b  in  1.109293  seconds.

    What is 1 / 1?
    A) 0
    B) 1
    C) 2
    D) 3
    b
    The student answered:  b  in  0.281228  seconds.

    What is 1 + 2?
    A) 0
    B) 1
    C) 2
    D) 3
    d
    The student answered:  d  in  1.218665  seconds.

    Is there another student taking the test? n

    This is the report for Bradley S student id number: 1111
    The student was flagged for cheating on question:  2
    The student was flagged for cheating on question:  3
    The student was flagged for cheating on question:  4
    The student was flagged for cheating on question:  5
    Number of flagged questions:  4 out of 5

    This is the report for brittany d student id number: 2222
    The student was flagged for cheating on question:  4
    Number of flagged questions:  1 out of 5
    
# Requirements

This program runs using Python 3.8, and utilizes the sys and datetime libraries. The input to file will change per user and stdin and stdout will be needed to input data and answer the questions.
