from flask import Flask, render_template, request
from analysis import load_data, medal_summary, top_countries, medal_trends, sport_summary

app = Flask(__name__)

def get_data():
    return load_data()

@app.route("/")
def index():
    try:
        athletes, data_note = get_data()
        season = request.args.get("season", "Summer")
        year = request.args.get("year", "All")
        filtered = athletes.copy()
        if season in ("Summer", "Winter"):
            filtered = filtered[filtered["Season"] == season]
        if year != "All":
            try:
                filtered = filtered[filtered["Year"] == int(year)]
            except ValueError:
                year = "All"

        summary = medal_summary(filtered)
        countries = top_countries(filtered, 10)
        trends = medal_trends(filtered)
        sports = sport_summary(filtered, 10)
        years = sorted(athletes["Year"].dropna().astype(int).unique().tolist())
        return render_template(
            "index.html",
            summary=summary,
            countries=countries,
            trends=trends,
            sports=sports,
            years=years,
            selected_year=year,
            selected_season=season,
            data_note=data_note,
        )
    except FileNotFoundError as exc:
        return render_template("setup.html", message=str(exc)), 200

if __name__ == "__main__":
    app.run(debug=True)
