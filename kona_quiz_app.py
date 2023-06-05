quiz = {
    "question1": {
        "question": "What is my name?",
        "answer": "Soheli Arefin kona"
    },

    "question2": {
          "question": "Where does she live?",
          "answer": "Bangladesh"
    },
    "question3": {
        "question": "What is the name of our national fish?",
        "answer": "Pang gash"
    },
    "question4": {
        "question": "What is Kona's favorite food?",
        "answer": "Egg"
    },
    "question5": {
        "question": "What is her favorite pasttime?",
        "answer": "Sleeping and watching cat videos."
    },
    "question6": {
        "question": "What is cats favourite food?",
        "answer": "Fish"
      
    },
    "question7": {
        "question": "Who is Charlotte Flair?",
        "answer": "American Wrestler"
    },
    "question8": {
        "question": "Who is the president of United States of America?",
        "answer": "Joe Biden"
    },
    "question9": {
        "question": "Who is the best islamic scholar?",
        "answer": "Maulana Tarik Jamil"
    },
    "question10": {
        "question": "How many legs does a cow have?",
        "answer": "4"
    },
}

score = 0

for key, value in quiz.items():
    print(value['question'])
    answer = input("Answer ")

    if answer.lower() == value['answer'].lower():
        print("Correct")
        score = score + 1
        print("Your score is :"  + str(score))
        print("")
        print("")


    else: 
        print("Wrong!")
        print("The answer is : " + value['answer'])
        print("your score is : " + str(score))    
        print("")
        print("")

    print("You got " + str(score) + " out of 10 question currectly")