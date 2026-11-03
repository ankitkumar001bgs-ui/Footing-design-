"""
AI-FOOTING DESIGN SOFTWARE

Module: Footing Design
Purpose: Preliminary isolated footing area calculation
"""

def calculate_footing_area(column_load, soil_bearing_capacity):

    if column_load <= 0:
        raise ValueError("Column load must be positive.")

    if soil_bearing_capacity <= 0:
        raise ValueError("Soil bearing capacity must be positive.")

    required_area = column_load / soil_bearing_capacity

    return required_area


# Test the calculation
if __name__ == "__main__":

    column_load = 1000
    soil_bearing_capacity = 200

    area = calculate_footing_area(
        column_load,
        soil_bearing_capacity
    )

    print("AI-FOOTING DESIGN SOFTWARE")
    print("-------------------------")
    print("Column Load:", column_load, "kN")
    print("Soil Bearing Capacity:", soil_bearing_capacity, "kN/m2")
    print("Required Footing Area:", area, "m2")
