from clean_data import load_and_clean_data
from print_stat import print_statistics
from plot_data import plot_photos_by_weather, plot_mood_distribution, plot_photos_over_time

def main():
    # Step 1: Load and clean
    df = load_and_clean_data("travel_data.csv")

    # Step 2: Print stats
    print_statistics(df)

    # Step 3: Plot
    plot_photos_by_weather(df)
    plot_mood_distribution(df)
    plot_photos_over_time(df)

if __name__ == "__main__":
    main()
