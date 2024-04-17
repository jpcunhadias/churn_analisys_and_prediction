import pandas as pd
import pytest

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.data.make_dataset import preprocess_data

def test_preprocess_data():
    # Create a sample input DataFrame
    data = pd.DataFrame({
        'customerID': ['1', '2', '3'],
        'Churn': ['Yes', 'No', 'Yes'],
        'TotalCharges': [100, None, 200],
        'gender': ['Male', 'Female', 'Male'],
        'Partner': ['Yes', 'No', 'Yes'],
        'Dependents': ['No', 'Yes', 'No']
    })

    # Expected output after preprocessing
    expected_output = pd.DataFrame({
        'Churn': [1, 0, 1],
        'TotalCharges': [100.0, 0.0, 200.0],
        'gender': [0, 1, 0],
        'Partner': [1, 0, 1],
        'Dependents': [0, 1, 0]
    })

    # Call the preprocess_data function
    processed_data = preprocess_data(data)

    # Assert that the processed data matches the expected output
    pd.testing.assert_frame_equal(processed_data, expected_output)

# Run the test
pytest.main()