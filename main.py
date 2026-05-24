import os
import pandas as pd
import json
from pathlib import Path
from embedding import embedding_func
from dotenv import load_dotenv
load_dotenv() 


def file_check(INPUT_FILE):
# -------------------------------
# LOAD CSV / XLS / XLSX
# -------------------------------

    file_ext = Path(INPUT_FILE).suffix.lower()

    if file_ext == ".csv":
        df = pd.read_csv(INPUT_FILE)
        return df
    elif file_ext in [".xls", ".xlsx"]:
        df = pd.read_excel(INPUT_FILE)
        return df
    else:
        raise ValueError("Unsupported file format. Use CSV or XLS/XLSX")
    
def check_validations(df, EXPECTED_COLUMNS):

    # -------------------------------
    # VALIDATE COLUMNS
    # -------------------------------

    missing_cols = [
        col for col in EXPECTED_COLUMNS
        if col not in df.columns
    ]

    if missing_cols:
        raise ValueError(
            f"Missing columns: {missing_cols}"
        )

    return True

def convert_to_json(df ,OUTPUT_FILE):
# -------------------------------
# CONVERT TO JSON
# -------------------------------

    # Replace NaN with empty string
    df = df.fillna("")

    # Convert dataframe to list of dictionaries
    records = df.to_dict(orient="records")

    # Save JSON
    with open(OUTPUT_FILE, "w", encoding="utf-8") as json_file:
        json.dump(records, json_file, indent=4, ensure_ascii=False, default=str)

    print(f"JSON exported successfully -> {OUTPUT_FILE}")

if __name__=="__main__":
    
    INPUT_FILE=os.getenv("INPUT_FILE")
    OUTPUT_FILE=os.getenv("OUTPUT_FILE")

    # -------------------------------
    # EXPECTED COLUMNS
    # -------------------------------

    EXPECTED_COLUMNS = [
        "MS ticket number",
        "subscription name",
        "Service",
        "title",
        "Serverity",
        "severity_raw",
        "created_date",
        "resolution_hours",
        "resolution_days",
        "status",
        "issue_summary",
        "root_cause",
        "resolution_summary",
        "analysis",
        "what_went_wrong",
        "best_practices"
    ]

    df=file_check(INPUT_FILE)
    is_valid = check_validations(df, EXPECTED_COLUMNS)

    if is_valid:
        convert_to_json(df, OUTPUT_FILE)
    embedding_func(OUTPUT_FILE)