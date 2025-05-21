# Diagnostic Test Probability Calculator

This is a simple Python tool I built to help calculate how likely it is that a patient has a disease, based on their test result. It uses Bayes' Theorem, which is basically a way of updating what we know (like disease prevalence) when we get new evidence (like a test result).

## What it does

You enter three things:

- **Prevalence** – how common the disease is in the population.
- **Sensitivity** – how good the test is at detecting people who actually have the disease.
- **Specificity** – how good the test is at correctly identifying people who don’t have it.

The program then tells you two probabilities:

- The chance someone has the disease **if they test positive**.
- The chance someone still has the disease **even if they test negative**.

In a clinical setting, this calculator can help doctors quickly estimate how likely it is that a patient actually has a disease after a test result, especially for screening. It gives a clearer picture than just looking at sensitivity or specificity alone.

However, it has limitations — it assumes the input values are accurate and doesn't account for patient symptoms, test variability, or multiple tests over time. It also can't replace clinical judgment, but it's a useful tool to support it.

