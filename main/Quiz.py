from string import ascii_lowercase
import random

## Defining direct requirements for method
NUM_QUESTIONS_PER_QUIZ = 5
QUESTIONS = {
    "In what year was Minecraft fully released?": [
        "2011", "2009", "2015", "2021"
    ],
    "Minecraft has been used in educational environments to teach computer science, computer-aided design, and what other subject?": [
        "Chemistry", "Math", "Geography", "Language"
    ],
    "What is the mobile version of the game called?": [
        "Minecraft Earth", "Minecraft Bedrock", "Minecraft Java", "Minecraft Mobile"
    ],
    "What was the game intially going to be called?": [
        "Cave Game",
        "Block Boy",
        "Machine Mining",
        "Mineblock",
    ],
    "Which species began due to a coding error?": [
        "Creeper",
        "Skeleton",
        "Chicken",
        "Bee",
    ],
    "How long did it take developers to create the first version of Minecraft?": [
        "6 days",
        "3 years",
        "1 year",
        "6 months",
    ],
    "Which country had Minecraft become mandatory in it's cirriculum?": [
        "Sweden",
        "Norway",
        "UK",
        "Irelenad",
    ],
    "What problem does tonic cure?": [
        "Nausea",
        "Tiredness",
        "Hunger",
        "Mining fatigue",
    ],
    "What do Evokers drop?": [
        "Totems of undying",
        "High tier enchants",
        "Experience orb",
        "Gold ingots",
    ],
    "A Husk is a type of zombie found in only one place. Where is this?": [
        "Desert",
        "Arctic",
        "Deep cave systems",
        "Jungle",
    ],
}

## OVERALL STRUCTURE
def run_quiz():
    questions = prepare_questions(QUESTIONS, num_questions=NUM_QUESTIONS_PER_QUIZ)

    num_correct = 0
    for num, (question, alternatives) in enumerate(questions, start=1):
        print(f"\nQuestion {num}:")
        num_correct += ask_question(question, alternatives)

    print(f"\nYou got {num_correct} correct out of {num} questions")

    #Add quit statement
    print("Thank you for playing! Please type quit to exit.")
    while (text := input()) != "quit":
        print("Please type quit to exit the program.")
         

##METHODS TO RUN
# Defining question selection, taking the arguements of questions and minimum samples(question iterations) to form
def prepare_questions(questions, num_questions):
    num_questions = min(num_questions, len(questions))
    return random.sample(list(questions.items()), k=num_questions)

# Defining question method, taking the list of questions alternatives, and returning integer outputs based on if input was correct/incorrect.
def ask_question(question, alternatives):
    correct_answer = alternatives[0]
    ordered_alternatives = random.sample(alternatives, k=len(alternatives))

    answer = get_answer(question, ordered_alternatives)
    if answer == correct_answer:
        print("⭐ Correct! ⭐")
        return 1
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}")
        return 0

# Defining answer return, taking question and alternatives as arguements
def get_answer(question, alternatives):
    print(f"{question}")
    labeled_alternatives = dict(zip(ascii_lowercase, alternatives))
    for label, alternative in labeled_alternatives.items():
        print(f"  {label}) {alternative}")

    while (answer_label := input("\nChoice? ")) not in labeled_alternatives:
        print(f"Please answer one of {', '.join(labeled_alternatives)}")

    return labeled_alternatives[answer_label]

# Starts application (i.e. runs when called as script but not upon import)
if __name__ == "__main__":
    run_quiz()
