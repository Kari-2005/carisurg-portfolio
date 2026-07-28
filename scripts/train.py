"""
Command-line training entry point for the Mercer emergency triage model.

The script reads the selected predictors, model settings, data path and output
locations from config.yaml. It then prepares the data, trains the pinned
Logistic Regression model and saves the fitted pipeline and evaluation results.
"""

import argparse
import sys
from pathlib import Path

import joblib


PROJECT_ROOT = Path(__file__).resolve().parents[1]

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


from src.data import load_data
from src.data import split_data
from src.features import prepare_features
from src.model import build_model
from src.model import evaluate_model
from src.model import train_model
from src.utils import create_output_directory
from src.utils import load_config
from src.utils import save_metrics


def parse_arguments():
    """
    Read command-line arguments supplied by the user.

    Returns
    -------
    argparse.Namespace
        Parsed command-line arguments.
    """
    parser = argparse.ArgumentParser(
        description=(
            "Train and evaluate the Mercer emergency triage model."
        )
    )

    parser.add_argument(
        "--config",
        default="config.yaml",
        help="Path to the YAML configuration file.",
    )

    return parser.parse_args()


def resolve_project_path(path_value):
    """
    Resolve a configured path relative to the project root.

    Parameters
    ----------
    path_value : str or pathlib.Path
        Path supplied through config.yaml.

    Returns
    -------
    pathlib.Path
        Absolute path used by the training script.
    """
    configured_path = Path(path_value)

    if configured_path.is_absolute():
        return configured_path

    return PROJECT_ROOT / configured_path


def run_training(config_path):
    """
    Run the complete model-training pipeline.

    Parameters
    ----------
    config_path : str or pathlib.Path
        Location of the YAML configuration file.
    """
    resolved_config_path = resolve_project_path(config_path)
    config = load_config(resolved_config_path)

    data_settings = config["data"]
    split_settings = config["split"]
    model_settings = config["model"]
    preprocessing_settings = config["preprocessing"]
    evaluation_settings = config["evaluation"]
    output_settings = config["outputs"]

    data_path = resolve_project_path(data_settings["path"])
    data = load_data(data_path)

    X, y = prepare_features(
        data=data,
        feature_names=data_settings["features"],
        target_name=data_settings["target"],
    )

    X_train, X_test, y_train, y_test = split_data(
        X=X,
        y=y,
        test_size=split_settings["test_size"],
        random_state=split_settings["random_state"],
    )

    model = build_model(
        hyperparameters=model_settings["hyperparameters"],
        standard_scaling=preprocessing_settings[
            "standard_scaling"
        ],
    )

    fitted_model, training_time_seconds = train_model(
        model=model,
        X_train=X_train,
        y_train=y_train,
    )

    _, metrics = evaluate_model(
        model=fitted_model,
        X_test=X_test,
        y_test=y_test,
        critical_class=evaluation_settings["critical_class"],
    )

    metrics["training_time_seconds"] = float(
        training_time_seconds
    )
    metrics["training_rows"] = int(len(X_train))
    metrics["testing_rows"] = int(len(X_test))
    metrics["selected_model"] = model_settings["name"]
    metrics["random_state"] = split_settings["random_state"]

    output_directory = create_output_directory(
        resolve_project_path(output_settings["directory"])
    )

    model_path = output_directory / output_settings["model_file"]
    metrics_path = (
        output_directory / output_settings["metrics_file"]
    )

    joblib.dump(fitted_model, model_path)
    save_metrics(metrics, metrics_path)

    print("Training completed successfully.")
    print(f"Selected model: {model_settings['name']}")
    print(f"Usable rows: {len(X)}")
    print(f"Training rows: {len(X_train)}")
    print(f"Testing rows: {len(X_test)}")
    print(f"Accuracy: {metrics['accuracy']:.3f}")
    print(f"Macro F1-score: {metrics['macro_f1']:.3f}")
    print(f"Weighted F1-score: {metrics['weighted_f1']:.3f}")
    print(f"ESI Level 1 recall: {metrics['esi_1_recall']:.3f}")
    print(f"Model saved to: {model_path}")
    print(f"Metrics saved to: {metrics_path}")


def main():
    """Run the training pipeline from the command line."""
    arguments = parse_arguments()
    run_training(arguments.config)


if __name__ == "__main__":
    main()
