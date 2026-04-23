import sys
from unittest.mock import MagicMock

# Mock pydantic before importing SevenLayerGuardian
mock_pydantic = MagicMock()
sys.modules["pydantic"] = mock_pydantic

import pytest
from backend.guce.guardian import SevenLayerGuardian

def test_calculate_sigma_squared_empty():
    guardian = SevenLayerGuardian()
    assert guardian.calculate_sigma_squared([]) == 0.0

def test_calculate_sigma_squared_single_item():
    guardian = SevenLayerGuardian()
    assert guardian.calculate_sigma_squared([0.95]) == 0.0

def test_calculate_sigma_squared_identical_items():
    guardian = SevenLayerGuardian()
    assert guardian.calculate_sigma_squared([0.9, 0.9, 0.9]) == 0.0

def test_calculate_sigma_squared_multiple_items():
    guardian = SevenLayerGuardian()
    # [1, 2, 3]
    # mean = 2
    # variance = ((1-2)^2 + (2-2)^2 + (3-2)^2) / 3 = (1 + 0 + 1) / 3 = 0.6666666666666666
    samples = [1.0, 2.0, 3.0]
    expected_variance = 2.0 / 3.0
    assert guardian.calculate_sigma_squared(samples) == pytest.approx(expected_variance)

def test_calculate_sigma_squared_floats():
    guardian = SevenLayerGuardian()
    samples = [0.95, 0.96, 0.88, 0.92, 0.89]
    # mean = (0.95 + 0.96 + 0.88 + 0.92 + 0.89) / 5 = 4.6 / 5 = 0.92
    # variance = ((0.95-0.92)^2 + (0.96-0.92)^2 + (0.88-0.92)^2 + (0.92-0.92)^2 + (0.89-0.92)^2) / 5
    # variance = (0.03^2 + 0.04^2 + (-0.04)^2 + 0^2 + (-0.03)^2) / 5
    # variance = (0.0009 + 0.0016 + 0.0016 + 0 + 0.0009) / 5 = 0.005 / 5 = 0.001
    assert guardian.calculate_sigma_squared(samples) == pytest.approx(0.001)
