import os
import pandas as pd

os.makedirs("data/features", exist_ok=True)

df = pd.read_csv("data/transformed/events.csv")

df["timestamp"] = pd.to_datetime(df["timestamp"])
df["duration_minutes"] = df["duration_seconds"] / 60
df["weekday"] = df["timestamp"].dt.day_name()

df.to_csv("data/features/events.csv", index=False)