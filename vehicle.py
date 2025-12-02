def vehicle_details(vehicle_number, owner_name, vehicle_type, year_of_manufacture):
    result = (
        f"Vehicle Number: {vehicle_number}\n"
        f"Owner Name: {owner_name}\n"
        f"Vehicle Type: {vehicle_type}\n"
        f"Year of Manufacture: {year_of_manufacture}\n"
    )
    return result

if __name__ == "__main__":
    vehicle_number = "KA31ca0541"
    owner_name = "bhumika"
    vehicle_type = "two wheeler"
    year_of_manufacture = 2020
    print(vehicle_details(vehicle_number, owner_name, 
                          vehicle_type, year_of_manufacture))
  from vehicle import vehicle_details

def test_vehicle_details():
    vehicle_number = "KA-01-1234"
    owner_name = "John Doe"
    vehicle_type = "Car"
    year_of_manufacture = 2020
    expected_output = (
        "Vehicle Number: KA-01-1234\n"
        "Owner Name: John Doe\n"
        "Vehicle Type: Car\n"
        "Year of Manufacture: 2020\n"
    )
    actual_output = vehicle_details(vehicle_number, owner_name, vehicle_type, year_of_manufacture)
    assert actual_output == expected_output
