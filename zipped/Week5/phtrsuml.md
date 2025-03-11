```mermaid
graph TD;
    %% Actors
    Citizen["👤 Citizen"] 
    Employee["👤 Public Works Employee"]
    Crew["👤 Repair Crew"]

    %% Use Cases
    UC1["🛠 Report Pothole"]
    UC2["📍 Track Pothole Status"]
    UC3["📄 Submit Damage Claim"]
    UC4["📌 Assign Repair Work"]
    UC5["🔄 Update Repair Status"]
    UC6["📊 Generate Repair Report"]

    %% Relationships
    Citizen -->|Reports| UC1
    Citizen -->|Tracks| UC2
    Citizen -->|Submits| UC3

    Employee -->|Assigns| UC4
    Employee -->|Generates| UC6

    Crew -->|Updates| UC5
    UC4 -->|Triggers| UC5