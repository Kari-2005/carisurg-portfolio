"""
Functions for constructing, training and evaluating the Mercer triage model.

The Week 8 pipeline reproduces the Logistic Regression model selected during
Week 7. Its hyperparameters are supplied through config.yaml so that the
training procedure remains consistent and reproducible.
"""

import time

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import f1_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


def build_model(hyperparameters, standard_scaling=True):
    """
    Construct the selected Logistic Regression model.

    Parameters
    ----------
    hyperparameters : dict
        Logistic Regression settings read from config.yaml.
    standard_scaling : bool, default=True
        Whether the predictors should be standardised before training.

    Returns
    -------
    sklearn.pipeline.Pipeline
        Untrained preprocessing and classification pipeline.
    """
    pipeline_steps = []

    if standard_scaling:
        pipeline_steps.append(("scaler", StandardScaler()))

    pipeline_steps.append(
        (
            "classifier",
            LogisticRegression(**hyperparameters),
        )
    )

    return Pipeline(pipeline_steps)


def train_model(model, X_train, y_train):
    """
    Fit the supplied model and record its training time.

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
        Fitted model and training time in seconds.
    """
    start_time = time.perf_counter()
    model.fit(X_train, y_train)
    training_time_seconds = time.perf_counter() - start_time

    return model, training_time_seconds


def evaluate_model(model, X_test, y_test, critical_class=1):
    """
    Evaluate the fitted multiclass model and record prediction time.

    Macro-averaged metrics are reported because the ESI classes are
    imbalanced. Precision and recall for ESI Level 1 are also reported
    because missed critical cases are especially important.

    Parameters
    ----------
    model : sklearn estimator
        Fitted model that provides a predict method.
    X_test : pandas.DataFrame or array-like
        Testing predictors.
    y_test : pandas.Series or array-like
        True testing labels.
    critical_class : int, default=1
        Label representing the most urgent ESI class.

    Returns
    -------
    tuple
        Predictions and a dictionary of evaluation results.
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

    labels = list(model.classes_)

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

    if critical_class in labels:
        critical_index = labels.index(critical_class)
        critical_precision = class_precision[critical_index]
        critical_recall = class_recall[critical_index]
    else:
        critical_precision = 0.0
        critical_recall = 0.0

    metrics = {
        "accuracy": float(accuracy_score(y_test, predictions)),
        "macro_precision": float(
            precision_score(
                y_test,
                predictions,
                average="macro",
                zero_division=0,
            )
        ),
        "macro_recall": float(
            recall_score(
                y_test,
                predictions,
                average="macro",
                zero_division=0,
            )
        ),
        "macro_f1": float(
            f1_score(
                y_test,
                predictions,
                average="macro",
                zero_division=0,
            )
        ),
        "weighted_f1": float(
            f1_score(
                y_test,
                predictions,
                average="weighted",
                zero_division=0,
            )
        ),
        "esi_1_precision": float(critical_precision),
        "esi_1_recall": float(critical_recall),
        "total_inference_time_seconds": float(
            total_inference_time
        ),
        "inference_time_per_patient_ms": float(
            inference_time_per_patient_ms
        ),
        "classification_report": classification_report(
            y_test,
            predictions,
            zero_division=0,
        ),
    }

    return predictions, metrics
