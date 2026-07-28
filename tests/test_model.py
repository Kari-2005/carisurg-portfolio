"""
Training smoke test for the Mercer emergency triage model.
"""

import numpy as np
import pandas as pd

from src.model import build_model
from src.model import evaluate_model
from src.model import train_model


def test_training_pipeline_runs_on_50_rows():
    """
    Confirm that the selected pipeline can train and predict on 50 rows.
    """
    random_generator = np.random.default_rng(seed=42)
    number_of_rows = 50

    X = pd.DataFrame(
        {
            "age": random_generator.integers(
                18,
                90,
                size=number_of_rows,
            ),
            "triage_vital_o2_device": random_generator.integers(
                0,
                2,
                size=number_of_rows,
            ),
            "triage_vital_o2": random_generator.integers(
                88,
                101,
                size=number_of_rows,
            ),
            "cc_chestpain": random_generator.integers(
                0,
                2,
                size=number_of_rows,
            ),
            "cc_shortnessofbreath": random_generator.integers(
                0,
                2,
                size=number_of_rows,
            ),
            "cc_alteredmentalstatus": random_generator.integers(
                0,
                2,
                size=number_of_rows,
            ),
            "triage_glucose": random_generator.integers(
                60,
                250,
                size=number_of_rows,
            ),
            "triage_vital_hr": random_generator.integers(
                50,
                150,
                size=number_of_rows,
            ),
            "triage_vital_rr": random_generator.integers(
                10,
                35,
                size=number_of_rows,
            ),
            "triage_vital_sbp": random_generator.integers(
                80,
                190,
                size=number_of_rows,
            ),
        }
    )

    y = pd.Series(
        np.tile([1, 2, 3, 4, 5], 10),
        name="esi",
    )

    model = build_model(
        hyperparameters={
            "max_iter": 1000,
            "random_state": 42,
        },
        standard_scaling=True,
    )

    fitted_model, training_time_seconds = train_model(
        model=model,
        X_train=X,
        y_train=y,
    )

    predictions, metrics = evaluate_model(
        model=fitted_model,
        X_test=X,
        y_test=y,
        critical_class=1,
    )

    assert len(predictions) == number_of_rows
    assert set(fitted_model.classes_) == {1, 2, 3, 4, 5}
    assert training_time_seconds >= 0
    assert 0.0 <= metrics["accuracy"] <= 1.0
    assert 0.0 <= metrics["macro_f1"] <= 1.0
    assert 0.0 <= metrics["esi_1_recall"] <= 1.0
