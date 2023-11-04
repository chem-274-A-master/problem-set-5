"""
Tests for IdealGas object.

volume units are liters
temperature is K
pressure are atm
"""

import math
import pytest

# import your ideal gas class here.


def test_class_attribute():

    # Change to name of your class if
    # different from IdealGas
    assert IdealGas.R == 0.082057


def test_pressure_1():
    volume = 22.41
    n_mols = 1
    temperature = 273.15
    expected_pressure = 1

    gas = IdealGas(volume=volume, n_mols=n_mols, temperature=temperature)

    # Check attributes
    assert gas.volume == volume
    assert gas.n_mols == n_mols
    assert gas.temperature == temperature

    assert math.isclose(gas.pressure, expected_pressure, abs_tol=0.01)


def test_pressure_2():
    volume = 22.41
    n_mols = 1
    temperature = 546.21
    expected_pressure = 2

    gas = IdealGas(volume=volume, n_mols=n_mols, temperature=temperature)

    # Check attributes
    assert gas.volume == volume
    assert gas.n_mols == n_mols
    assert gas.temperature == temperature

    assert math.isclose(gas.pressure, expected_pressure, abs_tol=0.01)


def test_pressure_3():
    volume = 10
    n_mols = 1.5
    temperature = 1000
    expected_pressure = 12.31

    gas = IdealGas(volume=volume, n_mols=n_mols, temperature=temperature)

    # Check attributes
    assert gas.volume == volume
    assert gas.n_mols == n_mols
    assert gas.temperature == temperature

    assert math.isclose(gas.pressure, expected_pressure, abs_tol=0.01)


def test_volume_error():
    """Test that gas cannot be constructed with zero volume."""

    # change the error type
    # you should create a custom error type
    with pytest.raises(YOURERRORTYPE):
        gas = IdealGas(volume=0, n_mols=1, temperature=273.15)


def test_error_setter():
    """Test that volume cannot be set to zero."""
    gas = IdealGas(volume=1.5, n_mols=0.5, temperature=150)

    # change the error type
    with pytest.raises(YOURERRORTYPE):
        gas.volume = 0


def test_pressure_error():
    """Test that we can't set the pressure"""
    gas = IdealGas(volume=1.5, n_mols=0.5, temperature=150)

    with pytest.raises(AttributeError):
        gas.pressure = 100


def test_setter():
    """Test that volume can be set"""
    gas = IdealGas(volume=1.5, n_mols=0.5, temperature=150)
    gas.volume = 1.25

    assert gas.volume == 1.25


def test_update_object():
    """Test that pressure is updated if volume is changed."""
    g = IdealGas(volume=22.41, n_mols=1, temperature=273.15)
    g.volume *= 2
    assert math.isclose(g.pressure, 0.5, abs_tol=0.1)


def test_add():
    """Test that ideal gases can be added together with correct results for properties.
    
    When two gasses are added, the resulting gas should have n_mols = n_mols1 + nmols2, v= v1 + v2, 
    and a temperature that is an average that is weighted by the number of moles of each gas.
    """

    gas1 = IdealGas(10, 3.25, 298.15)
    gas2 = IdealGas(30, 1.25, 273.15)

    added = gas1 + gas2

    assert added.volume == 40
    assert added.n_mols == 4.5
    assert math.isclose(added.temperature, 291.21, abs_tol=0.01)
