def print_statistics(df):
    print("Weather distribution:")
    print(df['weather'].value_counts())

    print("\nMood distribution:")
    print(df['mood'].value_counts())

    print("\nPhotos statistics:")
    print(df['photos'].describe())

    print("\nMissing values:")
    print(df.isnull().sum())
