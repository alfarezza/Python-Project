"""Linear Regression Module"""

# Import dependencies.
import numpy as np
# from ..utils.features import prepare_for_training


class LinearRegression:


    def __init__(
    self,
    data: np.ndarray,
    labels: np.ndarray,
    *,
    polynomial_degree: int = 0,
    sinusoid_degree: int = 0,
    normalize_data: bool = True
    ):
        """
        Linear regression constructor.

        :param data: training set (NumPy array).
        :param labels: training set outputs (NumPy array, same rows as data).
        :param polynomial_degree: degree of additional polynomial features.
        :param sinusoid_degree: multipliers for sinusoidal features.
        :param normalize_data: flag to normalize features.
        """
        if not isinstance(data, np.ndarray):
            raise ValueError("data must be a NumPy array")
        if not isinstance(labels, np.ndarray):
            raise ValueError("labels must be a NumPy array")
        if data.shape[0] != labels.shape[0]:
            raise ValueError("data and labels must have the same number of rows")

        # Feature engineering: expands, normalizes, and adds bias column
        data_processed, features_mean, features_deviation = prepare_for_training(
            data, polynomial_degree, sinusoid_degree, normalize_data
        )

        self.data = data_processed
        self.labels = labels
        self.features_mean = features_mean
        self.features_deviation = features_deviation
        self.polynomial_degree = polynomial_degree
        self.sinusoid_degree = sinusoid_degree
        self.normalize_data = normalize_data

        num_features = self.data.shape[1]
        self.theta = np.zeros((num_features, 1))