import pandas as pd

def load_and_clean_data(filename: str) -> pd.DataFrame:
    """
    Load travel data from a CSV file and clean it.

    - Removes rows with missing values
    - Filters out extreme outliers in the 'photos' column
    """
    # Load the CSV file
    df = pd.read_csv(filename)

    # Drop rows with any missing values
    df = df.dropna()

    # Remove rows where the number of photos is abnormally high (e.g., > 500)
    df = df[df['photos'] <= 500]

    return df

# Optional test
if __name__ == "__main__":
    df = load_and_clean_data("travel_data.csv")
    print(df.head())
