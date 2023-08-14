def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 0

    for question in questions:
        print("-------------------------")
        print(question)
        for option in options[question_num]:
            print(option)
        guess = input("Enter (A, B, C, or D): ").upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions[question], guess)
        question_num += 1

    display_score(correct_guesses, guesses)


def check_answer(answer, guess):
    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0


def display_score(correct_guesses, guesses):
    print("-------------------------")
    print("RESULTS")
    print("-------------------------")

    print("Answers: ", end="")
    for answer in questions.values():
        print(answer, end=" ")
    print()

    print("Guesses: ", end="")
    for guess in guesses:
        print(guess, end=" ")
    print()

    score = int((correct_guesses / len(questions)) * 100)
    print("Your score is: " + str(score) + "%")
    

def play_again():
    response = input("Do you want to play again? (yes or no): ").upper()
    return response == "YES"

questions = {
    "How many colours are in rainbow?": "D",
    "What is capital of INDIA?": "C",
    "Name of the biggest Planet is?": "B",
    "How far is the Sun from Earth?": "A"
}

options = (
    ("A. 6", "B. 9", "C. 2", "D. 7"),
    ("A. Haryana", "B. Jaipur", "C. Delhi", "D. Maharashtra"),
    ("A. Mercury", "B. Jupiter", "C. Neptune", "D. Saturn"),
    ("A. 151.98 million km", "B. 100.2 million km", "C. 276.8 million km", "D. 118.0 million km")
)

new_game()

while play_again():
    new_game()

print("Thank you for playing")
