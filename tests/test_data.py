"""
Sanity checks for loading and validating the Mercer triage data.
"""

import pandas as pd
import pytest

from src.data import load_data
from src.features import validate_schema


EXPECTED_FEATURES = [
    "age",
    "triage_vital_o2_device",
    "triage_vital_o2",
    "cc_chestpain",
    "cc_shortnessofbreath",
    "cc_alteredmentalstatus",
    "triage_glucose",
    "triage_vital_hr",
    "triage_vital_rr",
    "triage_vital_sbp",
]

TARGET_NAME = "esi"


def test_data_loading_and_expected_schema(tmp_path):
    """
    Confirm that a CSV can be loaded and contains the required model columns.
    """
    sample_data = pd.DataFrame(
        {
            "age": [35, 67],
            "triage_vital_o2_device": [0, 1],
            "triage_vital_o2": [98, 94],
            "cc_chestpain": [1, 0],
            "cc_shortnessofbreath": [0, 1],
            "cc_alteredmentalstatus": [0, 0],
            "triage_glucose": [100, 145],
            "triage_vital_hr": [82, 105],
            "triage_vital_rr": [18, 24],
            "triage_vital_sbp": [125, 102],
            "esi": [3, 2],
        }
    )

    test_file = tmp_path / "sample_triage_data.csv"
    sample_data.to_csv(test_file, index=False)

    loaded_data = load_data(test_file)

    validate_schema(
        data=loaded_data,
        feature_names=EXPECTED_FEATURES,
        target_name=TARGET_NAME,
    )

    expected_columns = set(EXPECTED_FEATURES + [TARGET_NAME])

    assert not loaded_data.empty
    assert expected_columns.issubset(loaded_data.columns)


def test_schema_validation_rejects_missing_column():
    """
    Confirm that schema validation fails loudly when a required column is absent.
    """
    incomplete_data = pd.DataFrame(
        {
            column: [1]
            for column in EXPECTED_FEATURES
            if column != "age"
        }
    )
    incomplete_data[TARGET_NAME] = [3]

    with pytest.raises(ValueError, match="age"):
        validate_schema(
            data=incomplete_data,
            feature_names=EXPECTED_FEATURES,
            target_name=TARGET_NAME,
        )
