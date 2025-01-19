def calculate_batting_average(plate_appearances, hits):
    """Calculate batting average given plate appearances and hits."""
    if plate_appearances == 0:
        return 0.0  # Avoid division by zero
    return round(hits / plate_appearances, 3)

# User input
try:
    plate_appearances = int(input("Enter the number of plate appearances: "))
    hits = int(input("Enter the number of hits: "))

    if plate_appearances < 0 or hits < 0:
        print("Plate appearances and hits must be non-negative integers.")
    elif hits > plate_appearances:
        print("Hits cannot exceed plate appearances.")
    else:
        batting_average = calculate_batting_average(plate_appearances, hits)
        print(f"The batting average is: {batting_average}")
except ValueError:
    print("Please enter valid integers for plate appearances and hits.")