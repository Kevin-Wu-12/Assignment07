import os
import pandas as pd

os.makedirs("data/clean", exist_ok=True)

df = pd.read_csv("data/raw/events.csv")

df = df.dropna()

valid_event_types = {"click", "login", "purchase", "scroll", "view"}
df = df[df["event_type"].isin(valid_event_types)]
df["duration_seconds"] = pd.to_numeric(
    df["duration_seconds"],
    errors="coerce"
)

df = df.dropna(subset=["duration_seconds"])

df["duration_seconds"] = df["duration_seconds"].astype(int)

df = df[df["duration_seconds"] > 0]

# clean timestamps
df["timestamp"] = pd.to_datetime(
    df["timestamp"],
    errors="coerce",
    format="mixed"
)

df = df.dropna(subset=["timestamp"])

df["timestamp"] = df["timestamp"].dt.strftime("%Y-%m-%dT%H:%M:%S")

df = df.dropna()

df.to_csv("data/clean/events.csv", index=False)