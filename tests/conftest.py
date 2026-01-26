
import pytest
import numpy as np
import pandas as pd
from unittest.mock import MagicMock

@pytest.fixture
def mock_returns():
    return np.random.randn(100, 5) * 0.01

@pytest.fixture
def mock_adj():
    return np.eye(5)

@pytest.fixture
def mock_features():
    return np.random.randn(5, 10)
