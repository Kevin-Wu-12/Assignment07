import pandas as pd
from datetime import datetime, timezone
import os
os.makedirs("data/clean", exist_ok=True)
df = pd.read_csv("data/raw/events.csv")


valid_event_types = {"click", "view", "purchase","buy","scroll"}
df = df[df["event_type"].isin(valid_event_types)]
df = df[df['duration_seconds'] >= 0]

df["timestamp"] = pd.to_datetime(df["timestamp"],format="mixed",
)
df = df.dropna(subset=["timestamp"])
df["timestamp"] = df["timestamp"].dt.strftime("%Y-%m-%dT%H:%M:%S")


df.to_csv("data/clean/events.csv", index=False)
print(df["event_type"].unique())