import marimo

__generated_with = "0.23.7"
app = marimo.App(width="medium")


@app.cell
def _():
    import pandas as pd
    import matplotlib.pyplot as plt

    df = pd.read_csv('data/features/events.csv')
    return df, plt


@app.cell
def _(df, plt):
    plt.hist(df["duration_minutes"], bins=20)
    plt.xlabel("Duration Minutes")
    plt.ylabel("Frequency")
    plt.title("Distribution of Event Durations")
    plt.show()
    return


if __name__ == "__main__":
    app.run()
