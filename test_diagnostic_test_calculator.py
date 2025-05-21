# test_diagnostic_test_calculator.py
from diagnostic_test_calculator import bayesian_update

def run_test_case(prevalence, sensitivity, specificity):
    pos, neg = bayesian_update(prevalence, sensitivity, specificity)
    print(f"Inputs: Prevalence={prevalence}%, Sensitivity={sensitivity}%, Specificity={specificity}%")
    print(f"  -> P(Disease | Test +): {pos:.2f}%")
    print(f"  -> P(Disease | Test -): {neg:.2f}%\n")

print("Running normal test cases:")
run_test_case(10, 90, 90)
run_test_case(50, 95, 85)
run_test_case(20, 70, 80)

print("Running edge test cases:")
run_test_case(0, 100, 100)     # No disease in population
run_test_case(100, 100, 100)   # Everyone has disease
run_test_case(5, 50, 50)       # Low accuracy test
