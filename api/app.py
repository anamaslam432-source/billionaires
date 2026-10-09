from flask import Flask, render_template
import pandas as pd
from datetime import date

app = Flask(__name__)


@app.route("/")
@app.route("/<d>")
def show(d=None):
    try:
        day = pd.to_datetime(d) if d else pd.Timestamp(date.today())
    except (ValueError, TypeError):
        return render_template(
            "index.html",
            day=pd.Timestamp(date.today()),
            people=[],
            error="Use a date like 2026-10-06.",
        )

    df = pd.read_excel("billionaires.xlsx", usecols="A:D")
    df.columns = ["name", "dob", "country", "networth"]
    df["dob"] = pd.to_datetime(df["dob"])

    match = df[(df["dob"].dt.month == day.month) & (df["dob"].dt.day == day.day)]

    people = [
        {
            "name": r["name"],
            "dob": r["dob"].date(),
            "country": r["country"],
            "networth": r["networth"],
        }
        for _, r in match.iterrows()
    ]

    return render_template("index.html", day=day, people=people, error=None)


if __name__ == "__main__":
    app.run(debug=True)
