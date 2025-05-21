# diagnostic_test_calculator.py

def bayesian_update(prevalence, sensitivity, specificity):
    # Convert percentages to probabilities
    p_disease = prevalence / 100
    p_test_positive_given_disease = sensitivity / 100
    p_test_negative_given_no_disease = specificity / 100
    
    # Calculate P(Test+)
    p_test_positive = (
        p_test_positive_given_disease * p_disease +
        (1 - p_test_negative_given_no_disease) * (1 - p_disease)
    )

    # Calculate P(Disease|Test+)
    if p_test_positive == 0:
        p_disease_given_test_positive = 0
    else:
        p_disease_given_test_positive = (
            p_test_positive_given_disease * p_disease / p_test_positive
        )

    # Calculate P(Test-)
    p_test_negative = (
        (1 - p_test_positive_given_disease) * p_disease +
        p_test_negative_given_no_disease * (1 - p_disease)
    )

    # Calculate P(Disease|Test-)
    if p_test_negative == 0:
        p_disease_given_test_negative = 0
    else:
        p_disease_given_test_negative = (
            (1 - p_test_positive_given_disease) * p_disease / p_test_negative
        )

    return p_disease_given_test_positive * 100, p_disease_given_test_negative * 100


def main():
    print("Welcome to the Diagnostic Test Probability Calculator")
    print("\nPlease enter the following information as percentages (from 0 to 100):")
    print("- Prevalence: How common the disease is in the population.")
    print("- Sensitivity: The test's ability to correctly detect the disease when it's present.")
    print("- Specificity: The test's ability to correctly rule out the disease when it's absent.\n")

    try:
        prevalence = float(input("Enter disease prevalence (%): "))
        sensitivity = float(input("Enter test sensitivity (%): "))
        specificity = float(input("Enter test specificity (%): "))

        if not (0 <= prevalence <= 100 and 0 <= sensitivity <= 100 and 0 <= specificity <= 100):
            raise ValueError("Values must be between 0 and 100.")

        prob_pos, prob_neg = bayesian_update(prevalence, sensitivity, specificity)

        print(f"\nIf the patient tests POSITIVE, the chance they actually have the disease is: {prob_pos:.2f}%")
        print(f"If the patient tests NEGATIVE, the chance they still have the disease is: {prob_neg:.2f}%")

    except ValueError as e:
        print("Invalid input:", e)


if __name__ == "__main__":
    main()
