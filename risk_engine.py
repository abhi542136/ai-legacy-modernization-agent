def assess_risk(code):

    risk = "LOW"
    reasons = []

    if "PWD=" in code or "UID=" in code:
        risk = "CRITICAL"
        reasons.append("HARDCODED_CREDENTIALS")

    if "SELECT *" in code:
        risk = "HIGH"
        reasons.append("RAW_SQL")

    if "On Error Resume Next" in code:
        if risk != "CRITICAL":
            risk = "MEDIUM"

        reasons.append("NO_ERROR_HANDLING")

    return {
        "risk_level": risk,
        "risk_reasons": reasons
    }