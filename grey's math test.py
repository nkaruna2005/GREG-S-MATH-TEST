import random
import time

# Function: create_question
def create_question(var_min_num, var_max_num):
    var_num1 = random.randint(var_min_num, var_max_num)
    var_num2 = random.randint(var_min_num, var_max_num)
    var_operator = random.choice(['+', '-'])
    return f"{var_num1} {var_operator} {var_num2}"

# Function: ask_question
def ask_question(var_question):
    var_start_time = time.time()
    var_answer = int(input(f"What is {var_question}? "))
    var_end_time = time.time()

    var_time_taken = int(var_end_time - var_start_time)
    var_correct_answer = eval(var_question)
    var_is_correct = (var_answer == var_correct_answer)

    return var_is_correct, var_time_taken

# Main program
def maths_test():
    print("Welcome to Greg's Maths Test!")

    # Difficulty selection
    while True:
        print("Select a difficulty:")
        print("1) Easy\n2) Medium\n3) Hard")
        var_choice = input("> ").lower()

        if var_choice in ["1", "e", "easy"]:
            var_questions = 5
            var_max_num = 10
            print("Easy mode selected!")
            break
        elif var_choice in ["2", "m", "medium"]:
            var_questions = 10
            var_max_num = 20
            print("Medium mode selected!")
            break
        elif var_choice in ["3", "h", "hard"]:
            var_questions = 15
            var_max_num = 50
            print("Hard mode selected!")
            break
        else:
            print("Invalid choice! Enter 1, 2 or 3.")

    var_score = 0
    var_results = []  # store (correct?, time)
    var_correct_count = 0

    for var_q in range(1, var_questions + 1):
        print(f"\nScore: {var_score}")
        print(f"Question {var_q} of {var_questions}:")

        # Final question = challenge
        if var_q == var_questions:
            print("Challenge question!")
            var_question = create_question(var_max_num, var_max_num * 2)
        else:
            var_question = create_question(var_max_num // 2, var_max_num)

        var_is_correct, var_time_taken = ask_question(var_question)

        if var_is_correct:
            # Points system: 10 - seconds (min 1)
            var_points = max(1, 10 - var_time_taken)
            var_score += var_points
            var_correct_count += 1
            print(f"Correct! You answered in {var_time_taken} second(s) - {var_points} point(s) awarded.")
        else:
            print(f"Incorrect! You answered in {var_time_taken} second(s) - no points awarded.")

        var_results.append((var_is_correct, var_time_taken))

    # Final results
    var_percentage = round((var_correct_count / var_questions) * 100)
    var_avg_time = round(sum(t for _, t in var_results) / var_questions)

    print("\nResults:")
    print(f"Final score: {var_score}")
    print(f"Correct answers: {var_percentage}%")
    print(f"Average response time: {var_avg_time}s")

    if var_correct_count == var_questions:
        print("You're a Maths Master!")

    print("\nBreakdown:")
    print("Question  Correct  Time")
    print("--------  -------  ----")
    for i, (c, t) in enumerate(var_results, start=1):
        var_correct_text = "Yes" if c else "No"
        print(f"{i:<8}  {var_correct_text:<7}  {t}s")

# Run the program
if __name__ == "__main__":
    maths_test()
