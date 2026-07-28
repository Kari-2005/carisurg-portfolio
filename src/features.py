"""
Feature preparation functions for the Mercer emergency triage model.

The final model uses the same ten triage-time predictors selected during
Weeks 6 and 7. This module checks the required schema, converts values to
numeric form and removes rows that cannot be used for model training.
"""

import numpy as np
import pandas as pd


def validate_schema(data, feature_names, target_name):
    """
    Check that the dataset contains the configured predictors and target.

    Parameters
    ----------
    data : pandas.DataFrame
        Complete emergency triage dataset.
    feature_names : list of str
        Predictor column names specified in config.yaml.
    target_name : str
        Target column specified in config.yaml.

    Raises
    ------
    ValueError
        If one or more required columns are missing.
    """
    required_columns = list(feature_names) + [target_name]

    missing_columns = [
        column
        for column in required_columns
        if column not in data.columns
    ]

    if missing_columns:
        raise ValueError(
            "The dataset is missing required columns: "
            + ", ".join(missing_columns)
        )


def prepare_features(data, feature_names, target_name):
    """
    Prepare the configured predictors and ESI target.

    Required columns are converted to numeric values. Infinite values are
    treated as missing, and rows containing missing predictors or targets are
    removed to reproduce the Week 7 modelling procedure.

    Parameters
    ----------
    data : pandas.DataFrame
        Complete emergency triage dataset.
    feature_names : list of str
        Predictor column names specified in config.yaml.
    target_name : str
        Name of the ESI target column.

    Returns
    -------
    tuple
        Predictor DataFrame and target Series.
    """
    validate_schema(data, feature_names, target_name)

    selected_columns = list(feature_names) + [target_name]
    prepared_data = data[selected_columns].copy()

    prepared_data = prepared_data.replace(
        [np.inf, -np.inf],
        np.nan,
    )

    for column in selected_columns:
        prepared_data[column] = pd.to_numeric(
            prepared_data[column],
            errors="coerce",
        )

    prepared_data = prepared_data.dropna(
        subset=selected_columns
    )

    valid_esi_levels = [1, 2, 3, 4, 5]
    prepared_data = prepared_data[
        prepared_data[target_name].isin(valid_esi_levels)
    ]

    if prepared_data.empty:
        raise ValueError(
            "No usable rows remain after preparing the "
            "configured predictors and target."
        )

    X = prepared_data[feature_names].copy()
    y = prepared_data[target_name].astype(int).copy()

    return X, y
