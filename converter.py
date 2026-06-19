import logging
import argparse
import pandas as pd

# Configure logging
logging.basicConfig(
    filename="logs.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def read_csv_file(input_file):
    """Read the CSV file."""
    return pd.read_csv(input_file)


def clean_data(df):
    """Handle missing values and parse dates."""
    for col in df.columns:
        if pd.api.types.is_numeric_dtype(df[col]):
            df[col] = df[col].fillna(0)
        else:
            df[col] = df[col].fillna("Not Available")

    if "DOB" in df.columns:
        df["DOB"] = pd.to_datetime(df["DOB"], errors="coerce")

    return df


def rename_columns(df):
    """Rename columns."""
    rename_dict = {
        "Name": "Full_Name",
        "DOB": "Birth_Date"
    }

    df.rename(columns=rename_dict, inplace=True)
    return df


def export_to_excel(df, output_file):
    """Export DataFrame to Excel."""
    df.to_excel(output_file, index=False)


def main():
    parser = argparse.ArgumentParser(
        description="Convert CSV files to Excel format"
    )

    parser.add_argument(
        "-i", "--input",
        required=True,
        help="Input CSV file"
    )

    parser.add_argument(
        "-o", "--output",
        required=True,
        help="Output Excel file"
    )

    args = parser.parse_args()

    try:
        logging.info("Program started")

        df = read_csv_file(args.input)
        df = clean_data(df)
        df = rename_columns(df)
        export_to_excel(df, args.output)

        logging.info(f"Output saved to {args.output}")

        print("--------------------------------")
        print("CSV converted successfully!")
        print("Output file:", args.output)
        print("--------------------------------")

    except FileNotFoundError:
        logging.error("Input file not found")
        print("Error: File not found!")

    except pd.errors.EmptyDataError:
        logging.error("CSV file is empty")
        print("Error: CSV file is empty!")

    except Exception as e:
        logging.error(str(e))
        print("Error:", e)


if __name__ == "__main__":
    main()