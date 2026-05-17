import pandas as pd
def add_features(df):
    def grade(marks):
        if marks >= 90:
            return "A"
        elif marks >= 75:
            return "B"
        elif marks >= 50:
            return "C"
        else:
            return "Fail"
    df["grade"] = df["marks"].apply(grade)
    df["city_avg"] = df.groupby("city")["marks"].transform("mean")
    return df

def topper(df):
    return df.sort_values(by= "marks", ascending=False).head(3)

def top_city(df):
    return df.groupby("city")["marks"].mean().sort_values(ascending=False).head(1)

