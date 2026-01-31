from pathlib import Path

from loguru import logger
from tqdm import tqdm
import typer

from bc_version_control_assignment.config import PROCESSED_DATA_DIR, RAW_DATA_DIR

app = typer.Typer()


@app.command()
def main(
    # ---- REPLACE DEFAULT PATHS AS APPROPRIATE ----
    input_path: Path = RAW_DATA_DIR / "dataset.csv",
    output_path: Path = PROCESSED_DATA_DIR / "dataset.csv",
    # ----------------------------------------------
):
    import pandas as pd  # Top imports unchanged

    logger.info(f"Reading data from {input_path}")
    df = pd.read_csv(input_path)

    # Small cleaning step: drop the first column
    column_to_drop = df.columns[0]
    logger.info(f"Dropping column: {column_to_drop}")
    df = df.drop(columns=[column_to_drop])

    logger.info(f"Writing cleaned data to {output_path}")
    df.to_csv(output_path, index=False)

    logger.success("Processing dataset complete.")


if __name__ == "__main__":
    app()

