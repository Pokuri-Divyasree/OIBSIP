# BMI Calculator (Beginner Tier)
# Oasis Infobyte - Python Programming Internship


def get_positive_number(message):
    """Asks the user for a number until a valid positive number is entered."""
    while True:
        try:
            value = float(input(message))
            if value <= 0:
                print("Error: Please enter a number greater than 0.")
            else:
                return value
        except ValueError:
            print("Error: Please enter numbers only (example: 65 or 1.70).")


def calculate_bmi(weight, height):
    """BMI = weight (kg) / height (m) squared."""
    return weight / (height ** 2)


def get_category(bmi):
    """Returns the BMI category as per standard ranges."""
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


def main():
    print("=== BMI Calculator ===")

    while True:
        weight = get_positive_number("Enter your weight in kg: ")
        height = get_positive_number("Enter your height in metres (example 1.70): ")

        bmi = calculate_bmi(weight, height)
        category = get_category(bmi)

        print(f"\nYour BMI is: {bmi:.2f}")
        print(f"Category: {category}\n")

        again = input("Calculate again? (yes/no): ").strip().lower()
        if again != "yes":
            print("Thank you! Stay healthy.")
            break


if __name__ == "__main__":
    main()