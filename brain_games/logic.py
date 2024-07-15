import prompt


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print("Hello,", name)
    return name


def ask_question(question):
    answer = prompt.string(f"Question: {question}\nYour answer: ")
    return answer


def interpret_answer(response, correct_answer):
    if response == correct_answer:
        print("Correct!")
        return True
    else:
        print(f"'{response}' is wrong answer ;(."
              f" Correct answer was '{correct_answer}'")
        return False


def play_game(name, game_logic, question_text):
    print(question_text)
    i = 0
    while i < 3:
        question, correct_answer = game_logic()
        answer = ask_question(question)
        if not interpret_answer(answer, correct_answer):
            print(f"Let's try again, {name}!")
            return
        i += 1
    print(f"Congratulations, {name}!")
