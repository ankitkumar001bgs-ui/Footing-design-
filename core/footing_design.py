"""
AI-FOOTING
Preliminary Isolated Footing Calculator
"""

import math


def validate_inputs(column_load, soil_pressure):
    values = (column_load, soil_pressure)

    if not all(math.isfinite(v) for v in values):
        raise ValueError("Inputs must be finite numbers.")

    if column_load <= 0:
        raise ValueError("Column load must be positive.")

    if soil_pressure <= 0:
        raise ValueError("Soil pressure must be positive.")


def calculate_footing_area(column_load, soil_pressure):
    """
    Preliminary area estimate.

    Load: kN
    Allowable soil pressure: kN/m2
    Area: m2
    """

    validate_inputs(column_load, soil_pressure)

    return column_load / soil_pressure


def calculate_square_dimensions(required_area):
    if not math.isfinite(required_area) or required_area <= 0:
        raise ValueError("Area must be positive and finite.")

    side = math.ceil(math.sqrt(required_area) * 10) / 10

    return side, side


def calculate_design(column_load, soil_pressure):

    required_area = calculate_footing_area(
        column_load,
        soil_pressure
    )

    length, width = calculate_square_dimensions(
        required_area
    )

    provided_area = length * width

    return {
        "required_area": required_area,
        "length": length,
        "width": width,
        "provided_area": provided_area,
        "area_difference": provided_area - required_area
    }


if __name__ == "__main__":

    print("=" * 45)
    print("       AI-FOOTING SOFTWARE")
    print("       PRELIMINARY DESIGN")
    print("=" * 45)

    try:
        load = float(input("Enter column load (kN): "))
        pressure = float(
            input("Enter allowable soil pressure (kN/m2): ")
        )

        result = calculate_design(load, pressure)

        print("\n---------- RESULTS ----------")

        for key, value in result.items():
            print(f"{key}: {value:.2f}")

    except ValueError as error:
        print("Input error:", error)
