class Actor:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class UseCase:
    def __init__(self, name, description):
        self.name = name
        self.description = description

actors = [
    Actor("Citizen", "Reports potholes and submits damage claims."),
    Actor("Public Works Employee", "Manages pothole reports and assigns repair work."),
    Actor("Repair Crew", "Updates pothole repair status and logs repair details."),
]

use_cases = [
    UseCase("Report Pothole", "Citizen logs a pothole location and severity."),
    UseCase("Track Pothole Status", "Citizen checks repair status of reported pothole."),
    UseCase("Submit Damage Claim", "Citizen submits a claim for pothole-related damages."),
    UseCase("Assign Repair Work", "Public works employee assigns repair crews and prioritizes repairs."),
    UseCase("Update Repair Status", "Repair crew updates work progress and materials used."),
    UseCase("Generate Repair Report", "Public works employee generates a report on pothole repairs."),
]

def print_diagram_details():
    print("Actors:")
    for actor in actors:
        print(f"- {actor.name}: {actor.description}")
    
    print("\nUse Cases:")
    for use_case in use_cases:
        print(f"- {use_case.name}: {use_case.description}")
    
    print("\nUse Case Diagram Description:")
    print("The diagram consists of three main actors: Citizens, Public Works Employees, and Repair Crews.")
    print("Citizens interact with the system to report potholes, track their status, and submit damage claims.")
    print("Public Works Employees manage the reported potholes, assign repair tasks, and generate reports.")
    print("Repair Crews update the system with repair progress and details, ensuring real-time tracking.")

print_diagram_details()
