"""
Feature preparation functions for the Mercer emergency triage model.

The final model uses ten predictors available during triage. This module
selects those predictors, converts them to numeric values and separates
the predictors from the ESI target.
"""

import numpy as np
import pandas as pd


def validate_schema(data, feature_names, target_name):
    """
    Check that the dataset contains the required predictors and target.

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
        column for column in required_columns if column not in data.columns
    ]

    if missing_columns:
        raise ValueError(
            "The dataset is missing required columns: "
            + ", ".join(missing_columns)
        )


def prepare_features(data, feature_names, target_name):
    """
    Prepare the configured predictors and ESI target.

    Rows with a missing target are removed because they cannot be used for
    supervised model training. Predictor values are converted to numeric
    values, while missing predictor values are retained for imputation
    inside the modelling pipeline.

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

    prepared_data = data[feature_names + [target_name]].copy()
    prepared_data = prepared_data.replace([np.inf, -np.inf], np.nan)

    for column in feature_names:
        prepared_data[column] = pd.to_numeric(
            prepared_data[column],
            errors="coerce",
        )

    prepared_data[target_name] = pd.to_numeric(
        prepared_data[target_name],
        errors="coerce",
    )

    prepared_data = prepared_data.dropna(subset=[target_name])

    valid_esi_levels = [1, 2, 3, 4, 5]
    prepared_data = prepared_data[
        prepared_data[target_name].isin(valid_esi_levels)
    ]

    if prepared_data.empty:
        raise ValueError(
            "No usable rows remain after preparing the features and target."
        )

    X = prepared_data[feature_names]
    y = prepared_data[target_name].astype(int)

    return X, y
