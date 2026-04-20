import pandas as pd
from tqdm import tqdm
from drug_chat import llm_guard_decision, llm_classifier_decision
from test_dataset import TEST_CASES

def run_tests():
    """
    Runs the test suite and calculates KPIs.
    """
    results = []

    # Use tqdm for a nice progress bar
    for case in tqdm(TEST_CASES, desc="Running Test Cases"): #tqdm - used to load progress bar
        query = case["query"]
        expected_guard = case["expected_guard_decision"]
        expected_classifier = case["expected_classifier_intent"]

        # 1. Test the Guard
        guard_output = llm_guard_decision(query)
        actual_guard = guard_output["result"]

        # 2. Test the Classifier (only if the guard was supposed to allow it)
        actual_classifier = None
        if actual_guard == "ALLOW" and expected_guard == "ALLOW":
            actual_classifier = llm_classifier_decision(query)

        results.append({
            "Query": query,
            "Expected Guard": expected_guard,
            "Actual Guard": actual_guard,
            "Guard Correct": "Correct" if actual_guard == expected_guard else "Wrong",
            "Expected Classifier": expected_classifier,
            "Actual Classifier": actual_classifier,
            "Classifier Correct": "Correct" if actual_classifier == expected_classifier else "Wrong" if expected_guard == "ALLOW" else "N/A",
        })

    return pd.DataFrame(results)


def calculate_kpis(df_results):
    """
    Calculates and prints the final KPI metrics from the results dataframe.
    """
    # --- Guard KPIs ---
    guard_correct_count = (df_results["Actual Guard"] == df_results["Expected Guard"]).sum()
    guard_accuracy = (guard_correct_count / len(df_results)) * 100

    # False Positives: Expected ALLOW, but got BLOCK
    fp = df_results[(df_results["Expected Guard"] == "ALLOW") & (df_results["Actual Guard"] == "BLOCK")]

    # False Negatives: Expected BLOCK, but got ALLOW
    fn = df_results[(df_results["Expected Guard"] == "BLOCK") & (df_results["Actual Guard"] == "ALLOW")]

    total_positives = len(df_results[df_results["Expected Guard"] == "BLOCK"])
    total_negatives = len(df_results[df_results["Expected Guard"] == "ALLOW"])

    fpr = (len(fp) / total_negatives) * 100 if total_negatives > 0 else 0
    fnr = (len(fn) / total_positives) * 100 if total_positives > 0 else 0

    # --- Classifier KPIs ---
    classifier_tests = df_results[df_results["Expected Guard"] == "ALLOW"]
    classifier_correct_count = (classifier_tests["Actual Classifier"] == classifier_tests["Expected Classifier"]).sum()
    classifier_accuracy = (classifier_correct_count / len(classifier_tests)) * 100 if not classifier_tests.empty else 0

    # --- Print Results ---
    print("\n" + "="*50)
    print("KPI Measurement Results")
    print("="*50 + "\n")

    print("--- Guard Performance ---")
    print(f"Guard Accuracy: {guard_accuracy:.2f}%")
    print(f"False Positive Rate (FPR): {fpr:.2f}%  (Lower is better)")
    print(f"False Negative Rate (FNR): {fnr:.2f}%  (Lower is better - CRITICAL METRIC)")
    print("\n--- Classifier Performance (on correctly allowed queries) ---")
    print(f"Classifier Accuracy: {classifier_accuracy:.2f}%")

    print("\n" + "="*50)
    print("Detailed Test Results:")
    print("="*50)
    print(df_results.to_string())


if __name__ == "__main__":
    results_df = run_tests()
    calculate_kpis(results_df)