# app/main.py

def validate_claim(claim):
    # Dummy validation for now
    if claim["claim_amount"] > 100000:
        return "Claim requires manual review."
    else:
        return "Claim approved automatically."

if __name__ == "__main__":
    sample_claim = {
        "patient_name": "John Doe",
        "treatment": "Appendectomy",
        "hospital": "XYZ Hospital",
        "claim_amount": 50000,
        "policy_id": "ABC123"
    }

    result = validate_claim(sample_claim)
    print("Validation Result:", result)
