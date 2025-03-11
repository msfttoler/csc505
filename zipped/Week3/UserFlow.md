```mermaid
stateDiagram-v2
    [*] --> Welcome
    Welcome --> Login
    Welcome --> Register
    Login --> ListOverview
    Register --> ListOverview
    
    ListOverview --> CreateList
    ListOverview --> ViewList
    
    CreateList --> EditList
    ViewList --> EditList
    
    EditList --> AddItems
    EditList --> RemoveItems
    EditList --> CheckItems
    
    AddItems --> EditList
    RemoveItems --> EditList
    CheckItems --> EditList
    
    EditList --> ListOverview