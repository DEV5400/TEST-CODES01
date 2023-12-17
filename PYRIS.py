import random
import os

class Pyris:
    FILENAME = "question_sets of pyris.txt"

    def __init__(self):
        self.question_sets = {}
        self.all_questions = {}  # Separate dictionary to store questions from all sets
        self.load_question_sets()

    def write_to_file(self):
        with open(self.FILENAME, 'w') as file:
            for set_serial_number, set_info in self.question_sets.items():
                file.write(f"{set_serial_number}:{set_info['name']}\n")
                for question, data in set_info['questions'].items():
                    file.write(f"{question}:{','.join(data['options'])}:{data['correct_answer']}\n")

    def load_question_sets(self):
        try:
            if os.path.exists(self.FILENAME):
                with open(self.FILENAME, 'r') as file:
                    lines = file.readlines()
                    set_serial_number = None
                    for line in lines:
                        parts = line.strip().split(':')
                        if len(parts) == 2:
                            set_serial_number, set_name = parts
                            self.question_sets[set_serial_number] = {'name': set_name, 'questions': {}}
                        elif len(parts) == 3 and set_serial_number:
                            question, options_str, correct_answer = parts
                            options = options_str.split(',')
                            self.question_sets[set_serial_number]['questions'][question] = {'options': options,
                                                                                            'correct_answer': int(
                                                                                                correct_answer)}
                            # Add the question to the separate dictionary
                            self.all_questions[question] = {'options': options,
                                                             'correct_answer': int(correct_answer)}
        except FileNotFoundError:
            self.question_sets = {}
            self.all_questions = {}

    def activate_mode(self, mode_name):
        print(f"\n----- PYRIS ACTIVATING {mode_name} MODE -----")

    def initialization_mode(self):
        self.activate_mode("INITIALIZATION")
        print("----- PYRIS INITIALIZATION MODE -----")
        # Add initialization logic here if needed

    def archive_mode(self):
        self.activate_mode("ARCHIVE")
        set_name = input("Enter the name for this question set: ").strip()
        set_serial_number = input("Enter the serial number for this question set: ").strip()
        questions = {}
        while True:
            question = input("Enter a question (or 'finish archive' to end): ").strip()
            if question.lower() == 'finish archive':
                break
            options = [input(f"Enter option {i + 1}: ").strip() for i in range(4)]
            correct_answer = int(input("Enter the correct option number: ").strip())
            questions[question] = {'options': options, 'correct_answer': correct_answer}
            # Also add the question to the separate dictionary
            self.all_questions[question] = {'options': options, 'correct_answer': correct_answer}
        self.question_sets[set_serial_number] = {'name': set_name, 'questions': questions}
        print(f"\nSet '{set_name}' (Serial No. {set_serial_number}) archived successfully.\n")
        self.write_to_file()

    def set_test_mode(self):
        self.activate_mode("SET-TEST")
        self.display_question_sets()
        set_serial_number = input("\nEnter the serial number of the question set you want to test: ").strip()

        selected_set = self.question_sets.get(set_serial_number)
        if selected_set:
            questions = selected_set['questions']
            self.run_test(questions)
        else:
            print(f"\nSet with serial number '{set_serial_number}' not found.\n")

    def burn_mode(self):
        self.activate_mode("BURN")
        if not self.question_sets:
            print("\nNo question sets available. Please archive sets first.\n")
            return

        self.display_question_sets()
        set_serial_number = input("\nEnter the serial number of the set to burn: ").strip()

        selected_set = self.question_sets.get(set_serial_number)
        if selected_set:
            print(f"\nSelected set: Serial No. {set_serial_number} - {selected_set['name']}\n")
            self.display_questions_in_set(set_serial_number)

            option = input("\nDo you want to delete a specific question from this set? (yes/no): ").strip().lower()
            if option == 'yes':
                self.delete_question_from_set(set_serial_number)
            else:
                del self.question_sets[set_serial_number]
                print(f"\nSet with serial number '{set_serial_number}' burned (deleted) successfully.\n")
                self.write_to_file()
        else:
            print(
                f"\nSet with serial number '{set_serial_number}' not found. Please enter a valid set serial number.\n")

    def delete_question_from_set(self, set_serial_number):
        question_to_delete = input("Enter the question you want to delete: ").strip()

        if question_to_delete in self.question_sets[set_serial_number]['questions']:
            del self.question_sets[set_serial_number]['questions'][question_to_delete]
            print(
                f"\nQuestion '{question_to_delete}' deleted from set '{self.question_sets[set_serial_number]['name']}' successfully.\n")
            self.write_to_file()
        else:
            print(f"\nQuestion '{question_to_delete}' not found in set. Please enter a valid question.\n")

    def run_test(self, questions):
        score = 0
        total_attempted = 0
        user_responses = {}

        for question, data in questions.items():
            print(question)
            for i, option in enumerate(data['options'], start=1):
                print(f"{i}. {option}")

            user_answer = int(input("Enter your answer (1-4, or 0 to skip): ").strip())
            if 1 <= user_answer <= 4:
                total_attempted += 1
                user_responses[question] = {'options': data['options'], 'user_answer': user_answer,
                                            'correct_answer': data['correct_answer']}
                if user_answer == data['correct_answer']:
                    score += 1

        print("\nTest results:")
        print(f"Your score: {score} out of {total_attempted}")
        if total_attempted > 0:
            percent_wrong = ((total_attempted - score) / total_attempted) * 100
            print(f"Percentage of Wrong Answers: {percent_wrong:.2f}%")

        # Display correct and user options for each question
        for question, response in user_responses.items():
            print("\nQuestion:", question)
            print("Correct Option:", response['options'][response['correct_answer'] - 1])
            print("Your Option:", response['options'][response['user_answer'] - 1])

    def jumble_mode(self):
        self.activate_mode("JUMBLE")
        # Shuffle the questions from the separate dictionary
        all_questions_keys = list(self.all_questions.keys())
        random.shuffle(all_questions_keys)
        self.run_test(
            {question: self.all_questions[question] for question in all_questions_keys})

    def display_question_sets(self):
        print("\nAvailable question sets:")
        for set_serial_number, set_info in self.question_sets.items():
            print(f"- Serial No. {set_serial_number}: {set_info['name']}")

    def display_questions_in_set(self, set_serial_number):
        print("\nQuestions in the set:")
        for question, data in self.question_sets[set_serial_number]['questions'].items():
            print(f"- {question}")

    def introduction_mode(self):
        self.activate_mode("INTRODUCTION")
        print("----- PYRIS ACTIVATING... -----")
        print("Welcome to PYRIS: Python Yielding Robust Integration Suite!")

    def user_guide_mode(self):
        print("\n----- PYRIS ACTIVATING USER GUIDE MODE -----")
        print("# PYRIS User Guide\n")
        print("## Introduction\n")
        print("Welcome to PYRIS: Python Yielding Robust Integration Suite! PYRIS is a Python-based program designed to help you create, test, and manage sets of questions for various purposes. Whether you're a teacher preparing quizzes or a student looking to practice, PYRIS is here to assist you.\n")
        print("## Getting Started\n")
        print("1. **Activation:**\n   - When you run PYRIS, you will see an activation message: \"----- PYRIS ACTIVATING... -----\"\n   - After the general activation, you will see: \"----- PYRIS ACTIVATING INITIALIZATION MODE -----\"\n")
        print("2. **Modes:**\n   - PYRIS operates in different modes, each serving a specific purpose.\n   - Modes are selected by entering the corresponding letter (I/A/B/C/D/E) when prompted.\n")
        print("3. **Available Modes:**\n   - **I. INTRODUCTION:** Display the initial welcome message.\n   - **A. ARCHIVE:** Create and archive sets of questions.\n   - **B. SET-TEST:** Test your knowledge with questions from a specific set.\n   - **C. JUMBLE:** Take a test with questions randomly selected from all available sets.\n   - **D. BURN:** Delete a specific question set.\n   - **E. EXIT:** Exit PYRIS.\n")
        print("## Mode Details\n")
        print("### A. ARCHIVE\n")
        print("- **Purpose:** Create and archive sets of questions.\n- **Procedure:**\n  1. Enter a name and serial number for the question set.\n  2. Input questions along with answer options.\n  3. To finish archiving, type \"finish archive\" when prompted for a question.\n")
        print("### B. SET-TEST\n")
        print("- **Purpose:** Test your knowledge with questions from a specific set.\n- **Procedure:**\n  1. Select a set by entering its serial number.\n  2. Answer questions presented in the test.\n")
        print("### C. JUMBLE\n")
        print("- **Purpose:** Take a test with questions randomly selected from all available sets.\n- **Procedure:**\n  - Questions from different sets are shuffled for a randomized test experience.\n")
        print("### D. BURN\n")
        print("- **Purpose:** Delete a specific question set.\n- **Procedure:**\n  1. Select a set by entering its serial number.\n  2. Decide whether to delete a specific question from the set.\n")
        print("### E. EXIT\n")
        print("- **Purpose:** Exit PYRIS.\n")
        print("## Additional Tips\n")
        print("- **Dynamic Question Addition:**\n  - While archiving a new set, you can dynamically add new questions, making PYRIS adaptable to future sets.\n")
        print("- **Error Handling:**\n  - PYRIS provides improved error handling for invalid inputs, ensuring a smoother user experience.\n")
        print("## Conclusion\n")
        print("PYRIS is designed to be user-friendly and versatile. Whether you're a teacher, student, or anyone seeking an interactive question management system, PYRIS has you covered. Explore the modes, create, and test your question sets effortlessly. Thank you for choosing PYRIS!\n")

    def main(self):
        self.introduction_mode()
        self.initialization_mode()

        while True:
            print("\nModes:")
            print("I. INTRODUCTION")
            print("A. ARCHIVE")
            print("B. SET-TEST")
            print("C. JUMBLE")
            print("D. BURN")
            print("E. EXIT")

            mode = input("Enter the mode (I/A/B/C/D/E): ").upper().strip()

            if mode == 'I':
                self.user_guide_mode()
            elif mode == 'A':
                self.archive_mode()
            elif mode == 'B':
                self.set_test_mode()
            elif mode == 'C':
                self.jumble_mode()
            elif mode == 'D':
                self.burn_mode()
            elif mode == 'E':
                print("Exiting PYRIS. Thank you!")
                break
            else:
                print("Invalid mode. Please enter I, A, B, C, D, or E.")

if __name__ == "__main__":
    pyris = Pyris()
    pyris.main()
