""" Module for testing dashboard
"""
from django.test import TestCase
from .app import infer_model

TEST_PATIENT_INPUT = [0, 4, 1, 2, 1, 1, 1, 1, 1, 0, 2, 1, 1, 1, 1, 1, 0, 1, 0, 1]


class InferTestCase(TestCase):
    """Class for testing the Model inference on the dashboard"""

    def test_infer_model_callback(self):
        """Function to test model inference callback with example patient"""
        n_clicks = 1
        output = infer_model(n_clicks, *TEST_PATIENT_INPUT)
        assert output[0] == "1.06%"
        assert output[1] == "98.94%"
