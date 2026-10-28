from pathlib import Path
import pandas as pd

DATA_DIR = Path(__file__).resolve().parent / "data"
ATHLETE_FILE = DATA_DIR / "athlete_events.csv"
NOC_FILE = DATA_DIR / "noc_regions.csv"

MEDALS = ["Gold", "Silver", "Bronze"]

def load_data():
    if not ATHLETE_FILE.exists():
        raise FileNotFoundError(
            "Dataset not found. Put athlete_events.csv and noc_regions.csv inside the data/ folder."
        )
    df = pd.read_csv(ATHLETE_FILE)
    note = "Analysis is based on athlete-event records in the supplied Olympic dataset."
    if NOC_FILE.exists():
        noc = pd.read_csv(NOC_FILE)
        if "NOC" in df.columns and "NOC" in noc.columns:
            keep = [c for c in ["NOC", "region", "notes"] if c in noc.columns]
            if keep:
                df = df.merge(noc[keep].drop_duplicates("NOC"), on="NOC", how="left")
    return df, note

def _medal_rows(df):
    return df[df["Medal"].isin(MEDALS)].copy() if "Medal" in df.columns else df.iloc[0:0].copy()

def medal_summary(df):
    rows = _medal_rows(df)
    counts = rows["Medal"].value_counts()
    return {
        "athlete_records": int(len(df)),
        "medal_records": int(len(rows)),
        "gold": int(counts.get("Gold", 0)),
        "silver": int(counts.get("Silver", 0)),
        "bronze": int(counts.get("Bronze", 0)),
        "countries": int(df["NOC"].nunique()) if "NOC" in df.columns else 0,
        "sports": int(df["Sport"].nunique()) if "Sport" in df.columns else 0,
    }

def top_countries(df, limit=10):
    rows = _medal_rows(df)
    if rows.empty or "NOC" not in rows.columns:
        return []
    result = rows.groupby("NOC").size().sort_values(ascending=False).head(limit)
    return [{"name": str(k), "count": int(v)} for k, v in result.items()]

def medal_trends(df):
    rows = _medal_rows(df)
    if rows.empty or "Year" not in rows.columns:
        return []
    result = rows.groupby(["Year", "Medal"]).size().reset_index(name="count")
    return [
        {"year": int(r.Year), "medal": str(r.Medal), "count": int(r["count"])}
        for _, r in result.sort_values(["Year", "Medal"]).iterrows()
    ]

def sport_summary(df, limit=10):
    rows = _medal_rows(df)
    if rows.empty or "Sport" not in rows.columns:
        return []
    result = rows.groupby("Sport").size().sort_values(ascending=False).head(limit)
    return [{"name": str(k), "count": int(v)} for k, v in result.items()]
