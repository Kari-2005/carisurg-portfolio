"""
Functions for loading and preparing the Mercer emergency triage dataset.

This module was created by refactoring the data-loading steps used in the
Week 6 and Week 7 notebooks. Further cleaning and validation functions will
be added before the Week 8 final submission.
"""

from pathlib import Path

import pandas as pd
from sklearn.model_selection import train_test_split


def load_data(file_path):
    """
    Load the emergency triage dataset from a CSV file.

    Parameters
    ----------
    file_path : str or Path
        Location of the CSV dataset.

    Returns
    -------
    pandas.DataFrame
        The loaded dataset.
    """
    file_path = Path(file_path)

    if not file_path.exists():
        raise FileNotFoundError(f"Dataset not found: {file_path}")

    data = pd.read_csv(file_path)

    if data.empty:
        raise ValueError("The loaded dataset is empty.")

    return data


def split_data(X, y, test_size=0.20, random_state=42):
    """
    Divide the features and target into stratified training and testing sets.

    Stratification is used to preserve the distribution of the ESI classes,
    including the relatively uncommon ESI Level 1 cases.
    """
    return train_test_split(
        X,
        y,
        test_size=test_size,
        random_state=random_state,
        stratify=y,
    )
