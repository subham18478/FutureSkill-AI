from flask import Flask, jsonify, render_template, request

from database import (
    initialize_database,
    add_skill_record,
    get_all_skill_records,
    get_future_skills as db_get_future_skills,
    get_declining_skills as db_get_declining_skills,
    get_reskilling_roles as db_get_reskilling_roles
)

from data_analysis import (
    load_data,
    get_future_skills,
    get_declining_skills,
    get_reskilling_roles
)

from model import analyze_skill_gaps


app = Flask(__name__, template_folder="templates")

# Initialize SQLite database
initialize_database()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analytics")
def analytics():
    return render_template("analytics.html")


@app.route("/settings")
def settings():
    return render_template("settings.html")


@app.route("/api/records", methods=["POST"])
def add_record():
    data = request.get_json()

    required_fields = [
        "industry",
        "process",
        "activity",
        "role",
        "current_skill"
    ]

    for field in required_fields:
        if not data.get(field):
            return jsonify({
                "error": f"{field} is required"
            }), 400

    add_skill_record(
        industry=data["industry"],
        process=data["process"],
        activity=data["activity"],
        role=data["role"],
        current_skill=data["current_skill"],
        ai_impact=data.get("ai_impact"),
        future_skill=data.get("future_skill"),
        skill_gap=data.get("skill_gap"),
        priority=data.get("priority"),
        recommendation=data.get("recommendation")
    )

    return jsonify({
        "success": True,
        "message": "Skill record added successfully"
    }), 201

@app.route("/api/data")
def data():
    return jsonify({
        "future_skills": get_future_skills().to_dict(),
        "declining_skills": get_declining_skills().to_dict(),
        "reskilling_roles": get_reskilling_roles().to_dict()
    })


@app.route("/api/skill-gaps")
def skill_gaps():
    df = load_data()

    results = analyze_skill_gaps(df)

    return jsonify(results)


@app.route("/api/future-skills")
def future_skills():
    return jsonify(
        get_future_skills().to_dict()
    )


@app.route("/api/declining-skills")
def declining_skills():
    return jsonify(
        get_declining_skills().to_dict()
    )


@app.route("/api/reskilling-roles")
def reskilling_roles():
    return jsonify(
        get_reskilling_roles().to_dict()
    )


# =========================
# DATABASE API
# =========================

@app.route("/api/records")
def records():
    """
    Return all persistent workforce intelligence
    records stored in SQLite.
    """

    records = get_all_skill_records()

    return jsonify(records)


if __name__ == "__main__":
    app.run(debug=True)