import random
import time

class MathsTest:
    def __init__(self):
        # Initialise variables for the game
        self.var_score = 0                  # Total score
        self.var_results = []               # Stores results (correct?, time)
        self.var_correct_count = 0          # Number of correct answers
        self.var_questions = 0              # Total number of questions
        self.var_max_num = 0                # Maximum number used in questions

    def choose_difficulty(self):
        """Ask the user to select difficulty and set questions + max number."""
        while True:
            print("Select a difficulty:")
            print("1) Easy\n2) Medium\n3) Hard")
            choice = input("> ").lower()

            if choice in ["1", "easy", "e"]:
                self.var_questions, self.var_max_num = 5, 10
                print("Easy mode selected!")
                break
            elif choice in ["2", "medium", "m"]:
                self.var_questions, self.var_max_num = 10, 20
                print("Medium mode selected!")
                break
            elif choice in ["3", "hard", "h"]:
                self.var_questions, self.var_max_num = 15, 50
                print("Hard mode selected!")
                break
            else:
                print("Invalid choice! Enter 1, 2 or 3.")

    def create_question(self, min_num, max_num):
        """Generate a random addition or subtraction question."""
        num1 = random.randint(min_num, max_num)
        num2 = random.randint(min_num, max_num)
        operator = random.choice(['+', '-'])

        # Ensure subtraction never produces a negative answer
        if operator == '-' and num1 < num2:
            num1, num2 = num2, num1

        return f"{num1} {operator} {num2}"

    def ask_question(self, question):
        """Ask the user the question, measure response time, and check correctness."""
        start = time.time()  # Start timing
        answer = int(input(f"What is {question}? "))  # User input
        end = time.time()    # End timing

        time_taken = int(end - start)  # Round down to nearest second
        correct_answer = eval(question)  # Evaluate expression
        return (answer == correct_answer), time_taken

    def play(self):
        """Main loop for running the maths test."""
        print("Welcome to Nethaya's Maths Test!")
        self.choose_difficulty()

        # Loop through all questions
        for q in range(1, self.var_questions + 1):
            print(f"\nScore: {self.var_score}")
            print(f"Question {q} of {self.var_questions}:")

            # Generate challenge question for the last one
            if q == self.var_questions:
                print("Challenge question!")
                question = self.create_question(self.var_max_num, self.var_max_num * 2)
            else:
                question = self.create_question(self.var_max_num // 2, self.var_max_num)

            # Ask question and check result
            correct, seconds = self.ask_question(question)

            if correct:
                # Award points: 10 - seconds (minimum 1 point)
                points = max(1, 10 - seconds)
                self.var_score += points
                self.var_correct_count += 1
                print(f"Correct! You answered in {seconds} second(s) - {points} point(s) awarded.")
            else:
                print(f"Incorrect! You answered in {seconds} second(s) - no points awarded.")

            # Save result for breakdown
            self.var_results.append((correct, seconds))

        # Show results after all questions
        self.show_results()

    def show_results(self):
        """Display the final score, percentage, average time, and breakdown."""
        percentage = round((self.var_correct_count / self.var_questions) * 100)
        avg_time = round(sum(t for _, t in self.var_results) / self.var_questions)

        print("\nResults:")
        print(f"Final score: {self.var_score}")
        print(f"Correct answers: {percentage}%")
        print(f"Average response time: {avg_time}s")

        # Special message if all correct
        if self.var_correct_count == self.var_questions:
            print("You're a Maths Master!")

        # Breakdown section
        print("\nBreakdown:")
        print("Question  Correct  Time")
        print("--------  -------  ----")
        for i, (c, t) in enumerate(self.var_results, start=1):
            print(f"{i:<8}  {'Yes' if c else 'No':<7}  {t}s")


# Run the program
if __name__ == "__main__":
    game = MathsTest()
    game.play()
