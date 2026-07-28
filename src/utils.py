"""
Shared helper functions for the Mercer emergency triage pipeline.

This module contains small reusable functions for loading the YAML
configuration, creating output folders and saving evaluation metrics.
"""

import json
from pathlib import Path

import yaml


def load_config(config_path):
    """
    Load the project configuration from a YAML file.

    Parameters
    ----------
    config_path : str or pathlib.Path
        Location of the YAML configuration file.

    Returns
    -------
    dict
        Project configuration settings.

    Raises
    ------
    FileNotFoundError
        If the configuration file cannot be found.
    ValueError
        If the configuration file is empty or invalid.
    """
    config_path = Path(config_path)

    if not config_path.exists():
        raise FileNotFoundError(
            f"Configuration file not found: {config_path}"
        )

    with config_path.open("r", encoding="utf-8") as config_file:
        config = yaml.safe_load(config_file)

    if not isinstance(config, dict):
        raise ValueError(
            "The configuration file is empty or does not contain "
            "valid settings."
        )

    return config


def create_output_directory(directory):
    """
    Create the configured output directory if it does not already exist.

    Parameters
    ----------
    directory : str or pathlib.Path
        Location where model outputs will be stored.

    Returns
    -------
    pathlib.Path
        Path to the output directory.
    """
    output_directory = Path(directory)
    output_directory.mkdir(parents=True, exist_ok=True)

    return output_directory


def save_metrics(metrics, file_path):
    """
    Save model evaluation metrics as a formatted JSON file.

    Parameters
    ----------
    metrics : dict
        Model evaluation results.
    file_path : str or pathlib.Path
        Destination of the JSON metrics file.
    """
    file_path = Path(file_path)
    file_path.parent.mkdir(parents=True, exist_ok=True)

    with file_path.open("w", encoding="utf-8") as metrics_file:
        json.dump(metrics, metrics_file, indent=4)
