import re
from utils import evaluate_password, display_feedback

def main():
    print("=" * 60)
    print("        PASSWORD COMPLEXITY CHECKER")
    print("=" * 60)

    while True:
        password = input("\nEnter Password: ")

        strength, score, feedback = evaluate_password(password)

        print("\nPassword Strength :", strength)
        print("Score             :", f"{score}/5")

        display_feedback(feedback)

        choice = input("\nCheck another password? (y/n): ").lower()

        if choice != 'y':
            print("\nThank you for using Password Complexity Checker!")
            break

if __name__ == "__main__":
    main()