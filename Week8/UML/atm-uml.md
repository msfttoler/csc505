```mermaid
stateDiagram-v2
    [*] --> Idle: Insert Card
    
    Idle --> Authentication: Card Inserted
    note right of Idle
        entry/Display Welcome
        exit/Read Card
    end note
    
    Authentication --> Authentication: EnterPIN [incorrect PIN] / increment error counter
    note right of Authentication
        entry/Request PIN
        exit/Verify PIN
    end note
    
    Authentication --> Rejected: CheckCounter [attempts > 3] / block card
    Authentication --> MainMenu: CheckPIN [correct PIN] / reset error counter
    
    MainMenu --> AccountInfo: Select Account Info
    MainMenu --> WithdrawMoney: Select Withdraw
    MainMenu --> Idle: Select Exit / eject card
    
    WithdrawMoney --> MainMenu: Select Back
    WithdrawMoney --> ProcessWithdrawal: Enter Amount
    
    ProcessWithdrawal --> DispenseCash: CheckBalance [sufficient funds] / deduct amount
    ProcessWithdrawal --> InsufficientFunds: CheckBalance [insufficient funds]
    
    DispenseCash --> CheckAccountStatus: Dispense Complete
    
    CheckAccountStatus --> AccountClosed: CheckBalance [balance = 0] / close account
    CheckAccountStatus --> MainMenu: CheckBalance [balance > 0]
    
    InsufficientFunds --> MainMenu: Acknowledge
    
    AccountInfo --> MainMenu: Return
    
    AccountClosed --> Idle: Account Closed / eject card
    
    Rejected --> [*]: Card Blocked