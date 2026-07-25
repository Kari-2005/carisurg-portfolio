"""
Functions for training and evaluating the Mercer triage models.

The Week 8 final pipeline will construct the selected Logistic Regression
model from the hyperparameters recorded in config.yaml. Keeping training and
evaluation in this module allows the same procedure to be reused by the
command-line training script and the sanity checks.
"""

import time

from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import f1_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score


def train_model(model, X_train, y_train):
    """
    Fit a supplied scikit-learn model and record its training time.

    Parameters
    ----------
    model : sklearn estimator
        Model that provides a fit method.
    X_train : pandas.DataFrame or array-like
        Training predictors.
    y_train : pandas.Series or array-like
        Training target labels.

    Returns
    -------
    tuple
        The fitted model and training time in seconds.
    """
    start_time = time.perf_counter()
    model.fit(X_train, y_train)
    training_time_seconds = time.perf_counter() - start_time

    return model, training_time_seconds


def evaluate_model(model, X_test, y_test, critical_class=1):
    """
    Evaluate a fitted multiclass model and record prediction time.

    Macro-averaged metrics are included because the ESI classes are
    imbalanced. Precision and recall for ESI Level 1 are reported separately
    because missed critical cases are especially important in this project.

    Parameters
    ----------
    model : sklearn estimator
        Fitted model that provides a predict method.
    X_test : pandas.DataFrame or array-like
        Testing predictors.
    y_test : pandas.Series or array-like
        True testing labels.
    critical_class : int, default=1
        Label used for the ESI Level 1 class.

    Returns
    -------
    tuple
        Predictions and a dictionary containing evaluation results.
    """
    start_time = time.perf_counter()
    predictions = model.predict(X_test)
    total_inference_time = time.perf_counter() - start_time

    number_of_patients = len(X_test)
    inference_time_per_patient_ms = (
        total_inference_time / number_of_patients * 1000
        if number_of_patients > 0
        else 0.0
    )

    labels = list(getattr(model, "classes_", []))
    if critical_class in labels:
        critical_index = labels.index(critical_class)
        class_precision = precision_score(
            y_test,
            predictions,
            labels=labels,
            average=None,
            zero_division=0,
        )
        class_recall = recall_score(
            y_test,
            predictions,
            labels=labels,
            average=None,
            zero_division=0,
        )
        esi_1_precision = class_precision[critical_index]
        esi_1_recall = class_recall[critical_index]
    else:
        esi_1_precision = 0.0
        esi_1_recall = 0.0

    metrics = {
        "accuracy": accuracy_score(y_test, predictions),
        "macro_precision": precision_score(
            y_test,
            predictions,
            average="macro",
            zero_division=0,
        ),
        "macro_recall": recall_score(
            y_test,
            predictions,
            average="macro",
            zero_division=0,
        ),
        "macro_f1": f1_score(
            y_test,
            predictions,
            average="macro",
            zero_division=0,
        ),
        "weighted_f1": f1_score(
            y_test,
            predictions,
            average="weighted",
            zero_division=0,
        ),
        "esi_1_precision": esi_1_precision,
        "esi_1_recall": esi_1_recall,
        "total_inference_time_seconds": total_inference_time,
        "inference_time_per_patient_ms": inference_time_per_patient_ms,
        "classification_report": classification_report(
            y_test,
            predictions,
            zero_division=0,
        ),
    }

    return predictions, metrics

