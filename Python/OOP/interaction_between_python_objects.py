latitude = float("40.09")
longitude = float("-3.47")

antipode_latitude = latitude.__mul__(int("-1"))
antipode_longitude = longitude.__add__(int("180"))
print(f"Antipode coordinates: {antipode_latitude}, {antipode_longitude}")
