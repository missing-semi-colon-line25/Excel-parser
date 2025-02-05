import pandas as pd

def parse_excel(file_path, columns, n):
    try:
        # Load the Excel file
        df = pd.read_excel(file_path)

        # Select specified columns
        df_selected = df[columns]

        # Print first 'n' records
        print(df_selected.head(n))
    except Exception as e:
        print(f"Error: {e}")


file_path = input("Enter file path")
columns = input("Enter the column names to fetch (comma-separated): ").strip().split(',')
n = 5  # Number of records to display
parse_excel(file_path, columns, n)
