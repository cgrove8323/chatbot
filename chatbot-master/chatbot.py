# PyChat 2K17

import random

def start():
    print('''                  _             _       _              (")                      ___    _                _                                     
               _ | |  _  _     | |     (_)    __ _      \|     ___      o O O  / __|  | |_     __ _    | |_      _ _    ___     ___    _ __   
              | || | | +| |    | |     | |   / _` |           (_-<     o      | (__   | ' \   / _` |   |  _|    | '_|  / _ \   / _ \  | '  \  
              _\__/   \_,_|   _|_|_   _|_|_  \__,_|   _____   /__/_   TS__[O]  \___|  |_||_|  \__,_|   _\__|   _|_|_   \___/   \___/  |_|_|_| 
            _|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|     |_|"""""| {======|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""| 
            "`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'./o--000'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-' ''')

def end():
    pass

def confirm(question):
    while True:
        answer = input(question + " (y/n)")
        answer = answer.lower()

        if answer in ["y" , "yes", "yup"]:
            return True
        elif answer in ["n", "no", "nope"]:
            return False
   
def has_keyword(statement, keywords):
    '''for word in keywords:
        if word in statement:
            return True

    return False'''

    words = statement.split()
    for i in words:
        if i in keywords:
            return True
        
    return False

def get_random_response():
    responses = ["Uh, huh.",
                 "Oh, that's interesting",
                 "Nice",
                 "You don't say",
                 "Wow, that's cool"]

    return random.choice(responses)

def get_response(statement):
    statement = statement.lower()
    
    family_words = ["mother", "father", "brother", "sister"]
    teacher_words = [" cooper "]
    greetings = ["hello", " hi", "howdy", "sup", "what's up"]
    compliments = ["you"]
    gratitude = ["thank"]
    welcome = ["welcome"]
    
    if has_keyword(statement, family_words):
        response = "Tell me more about your family."
    elif has_keyword(statement, teacher_words):
        response = "I hear Mr. Cooper's class is really fun."
    elif has_keyword(statement, greetings):
        response = "Well, hello to you too!"
    elif statement[-1] == "?":
        response = "That's an interesting question. I'm really not sure."
    elif has_keyword(statement, welcome):
        response = "So tell me about yourself."
    elif has_keyword(statement, gratitude):
        response = "You're welcome!"
    elif has_keyword(statement, compliments):
        response = "Thank you!"
    else:
        response = get_random_response()

    return response

def play():
    talking = True

    print("Hello. I'm Julia. What is your name?")
    name = input(">> ")
    print("Hello " + name + "!")
    print("Say something to me!")

    while talking:
        statement = input(">>" + name + ": ")

        if statement == "Goodbye":
            talking = False
        elif len(statement) == 0:
            print("Say something")
        else:
            response = get_response(statement)
            print("Julia: " + response)

    print("Goodbye. It was nice talking to you.")

start()

playing = True

while playing:
    play()
    playing = confirm("Would you like to chat again?")

end()
