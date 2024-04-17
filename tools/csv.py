import os
import pandas as pd
from settings import BASE_DIR


def read_csv_file(file_path: str):
    filePath = os.path.join(
        BASE_DIR,
        file_path,
    )

    df = pd.read_csv(filePath, delimiter=";")
    csv_data = df.to_dict(orient="records")
    return csv_data
