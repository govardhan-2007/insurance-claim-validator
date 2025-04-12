# app/main.py

import csv

def validate_claim(claim):
    if int(claim["claim_amount"]) > 100000:
        return f"❌ Claim by {claim['patient_name']} requires manual review."
    else:
        return f"✅ Claim by {claim['patient_name']} approved automatically."

def read_and_validate(filename):
    results = []
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            result = validate_claim(row)
            results.append(result)
    return results

if __name__ == "__main__":
    # Since GitHub won't run code, just simulate output
    print("This script validates health insurance claims from a CSV file.")
