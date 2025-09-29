import pytest
import numpy as np
from assets import robots, sensors

def test_robot_import():
    """Test that robots can be imported."""
    assert hasattr(robots, "__all__")

def test_sensor_import():
    """Test that sensors can be imported."""
    assert hasattr(sensors, "__all__")