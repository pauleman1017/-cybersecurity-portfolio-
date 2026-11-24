import re

def analyze_email(headers, body):
    score = 0
    reasons = []
    if "urgent" in body.lower():
        score += 2
        reasons.append("Urgency language")
    if re.search(r"http://", body):
        score += 2
        reasons.append("Insecure http link")
    if "verify your account" in body.lower():
        score += 3
        reasons.append("Credential harvesting phrase")
    print(f"Risk Score: {score}/10")
    print("Reasons:", reasons)

analyze_email("", "URGENT verify your account http://fake-login.com")
