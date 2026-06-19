# CSV to Excel Converter

A Python-based utility that converts CSV files into Excel (.xlsx) format while performing basic data cleaning and normalization.

## Features

- Read CSV files
- Handle missing values
- Parse date columns
- Rename columns
- Export data to Excel (.xlsx)
- Command-line interface using argparse
- Logging support
- Error handling for invalid or missing files

## Technologies Used

- Python
- Pandas
- Openpyxl
- Argparse
- Logging

## Installation

Install the required libraries:

```bash
pip install -r requirements.txt
```

## Usage

Run the program using:

```bash
python converter.py -i sample.csv -o output.xlsx
```

## Example

Input:

sample.csv

Output:

output.xlsx

## Project Structure

```
CSV_Excel_Converter/
│
├── converter.py
├── sample.csv
├── requirements.txt
├── README.md
└── logs.txt
```

## Author

Vidhi Kothari
