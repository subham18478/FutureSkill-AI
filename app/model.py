import pandas as pd


def calculate_skill_gap(row):
    """
    Calculate a simple skill-gap priority from the AI impact
    and current/future skill relationship.
    """

    impact = str(row["ai_impact"]).strip().lower()

    if impact == "declining":
        return "High"

    if impact == "increasing":
        return "Medium"

    return "Low"

def calculate_skill_gap_score(row):
    """
    Calculate a numeric skill-gap score based on AI impact.
    Higher score = greater need for reskilling.
    """

    impact = str(row["ai_impact"]).strip().lower()

    if impact == "declining":
        return 90

    if impact == "increasing":
        return 60

    if impact == "ai-augmented":
        return 30

    return 20


def generate_recommendation(row):
    """
    Generate a reskilling recommendation based on the
    current skill, AI impact and future skill.
    """

    current_skill = row["current_skill"]
    future_skill = row["future_skill"]
    impact = str(row["ai_impact"]).strip().lower()
    score = calculate_skill_gap_score(row)
    priority = calculate_skill_gap(row)

    if impact == "declining":
        message = (
            f"Consider transitioning from {current_skill} "
            f"towards {future_skill}."
        )

    elif impact == "increasing":
        message = (
            f"Strengthen {current_skill} and develop "
            f"{future_skill} capabilities."
        )

    else:
        message = (
            f"Maintain {current_skill} and explore "
            f"{future_skill}."
        )

    return {
        "current_skill": current_skill,
        "future_skill": future_skill,
        "ai_impact": row["ai_impact"],
        "score": score,
        "priority": priority,
        "recommendation": message
    }


def analyze_skill_gaps(dataframe):
    """
    Analyze every role/skill record and return
    structured skill-gap recommendations.
    """

    results = []

    for _, row in dataframe.iterrows():

        result = generate_recommendation(row)

        results.append(result)

    return results