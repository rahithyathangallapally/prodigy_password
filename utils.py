import re

def evaluate_password(password):

    score = 0
    feedback = []

    # Length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should contain at least 8 characters.")

    # Uppercase
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    # Lowercase
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    # Number
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Include at least one number.")

    # Special Character
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Include at least one special character.")

    # Rating
    if score == 5:
        strength = "Very Strong"

    elif score == 4:
        strength = "Strong"

    elif score == 3:
        strength = "Moderate"

    elif score == 2:
        strength = "Weak"

    else:
        strength = "Very Weak"

    return strength, score, feedback


def display_feedback(feedback):

    if len(feedback) == 0:
        print("\nExcellent! Your password satisfies all security requirements.")
    else:
        print("\nSuggestions:")
        for item in feedback:
            print("•", item)