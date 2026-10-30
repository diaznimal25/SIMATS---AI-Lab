# Experiment 12 - Pattern Matching in a Healthcare Symptom Assessment System
import re

symptom_patterns = {
    "Emergency Warning Signs": [
        r"\bchest pain\b", r"\bdifficulty breathing\b", r"\bshortness of breath\b",
        r"\bface drooping\b", r"\bsudden weakness\b", r"\bsevere bleeding\b",
    ],
    "Respiratory Symptoms": [
        r"\bcough\b", r"\bsore throat\b", r"\brunny nose\b", r"\bfever\b",
    ],
    "Digestive Symptoms": [
        r"\bnausea\b", r"\bvomiting\b", r"\bstomach pain\b",
        r"\babdominal pain\b", r"\bdiarrhea\b",
    ],
    "Neurological or General Symptoms": [
        r"\bheadache\b", r"\bdizziness\b", r"\bfatigue\b", r"\bweakness\b",
    ],
}

guidance = {
    "Emergency Warning Signs":
        "Seek emergency medical care immediately. Do not delay care while using this system.",
    "Respiratory Symptoms":
        "Consider professional medical advice if symptoms persist, worsen, "
        "or are accompanied by breathing difficulty.",
    "Digestive Symptoms":
        "Maintain hydration if appropriate and seek medical advice for "
        "persistent or worsening symptoms.",
    "Neurological or General Symptoms":
        "Consider medical assessment if symptoms persist or worsen. Sudden weakness "
        "or other sudden neurological changes require emergency assessment.",
}

def match_symptoms(patient_input):
    text = patient_input.lower()
    categories, symptoms = [], []
    for category, patterns in symptom_patterns.items():
        found = []
        for pattern in patterns:
            m = re.search(pattern, text)
            if m:
                found.append(m.group())
        if found:
            categories.append(category)
            symptoms.extend(found)
    return categories, symptoms

def healthcare_assistant():
    print("HEALTHCARE SYMPTOM ASSESSMENT SYSTEM")
    print("-" * 40)
    print("Describe the symptoms in one sentence.")
    print("Example: I have a fever, cough and sore throat.")
    patient_input = input("\nPatient: ").strip()

    if not patient_input:
        print("System: Please enter a symptom description.")
        return

    categories, symptoms = match_symptoms(patient_input)

    print("\nASSESSMENT REPORT")
    print("-" * 40)

    if not categories:
        print("Matched symptoms: None")
        print("System: No predefined pattern was matched.")
        print("Please describe the symptoms more clearly or consult a healthcare professional.")
        return

    print("Matched symptoms:", ", ".join(sorted(set(symptoms))))
    print("Matched categories:", ", ".join(categories))

    # Emergency patterns take priority
    if "Emergency Warning Signs" in categories:
        print("\nPriority: EMERGENCY WARNING SIGN")
        print("Guidance:", guidance["Emergency Warning Signs"])
    else:
        print("\nPriority: NON-EMERGENCY PATTERN MATCH")
        for category in categories:
            print(f"{category}: {guidance[category]}")

    print("\nNote: This system does not diagnose diseases "
          "or replace professional medical assessment.")

healthcare_assistant()
