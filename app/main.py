import os
from flask import Flask, jsonify, render_template
from data_analysis import (
    load_data,
    get_future_skills,
    get_declining_skills,
    get_reskilling_roles
)
from model import analyze_skill_gaps

app = Flask(__name__, template_folder="templates")


@app.route("/")
def home():
    return render_template("index.html")


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
    return jsonify(get_future_skills().to_dict())


@app.route("/api/declining-skills")
def declining_skills():
    return jsonify(get_declining_skills().to_dict())


@app.route("/api/reskilling-roles")
def reskilling_roles():
    return jsonify(get_reskilling_roles().to_dict())


if __name__ == "__main__":
    app.run(debug=True)