def generate_checklist(code):

    checklist = []

    if "PWD=" in code or "UID=" in code:
        checklist.append(
            "Replace hardcoded DB credentials with environment variables"
        )

    if "SELECT *" in code:
        checklist.append(
            "Replace raw SQL queries with parameterized ORM queries"
        )

    if "On Error Resume Next" in code:
        checklist.append(
            "Add proper try-catch exception handling"
        )

    checklist.append(
        "Add unit tests covering edge cases"
    )

    checklist.append(
        "Add logging and monitoring"
    )

    return checklist