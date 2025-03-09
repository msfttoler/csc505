class ATM:
    def __init__(self):
        # Initialize ATM state and variables
        self.state = "Idle"
        self.pin_attempts = 0
        self.max_attempts = 3
        self.account_balance = 500  # Starting balance for demo
        self.correct_pin = "1234"   # Demo PIN
        self.transaction_history = []
        
    def process_event(self, event, *args):
        """Process events and transition between states based on the state diagram"""
        print(f"\nCurrent State: {self.state}")
        print(f"Event: {event}")
        
        # State transitions based on current state and event
        if self.state == "Idle" and event == "Insert Card":
            print("Entry Action: Display Welcome Screen")
            print("Exit Action: Read Card Data")
            self.state = "Authentication"
            print(f"Transition to: {self.state}")
            
        elif self.state == "Authentication" and event == "Enter PIN":
            pin = args[0]
            print("Entry Action: Request PIN")
            
            if pin == self.correct_pin:
                print("Guard: [correct PIN]")
                print("Action: Reset error counter")
                self.pin_attempts = 0
                self.state = "MainMenu"
            else:
                print("Guard: [incorrect PIN]")
                print("Action: Increment error counter")
                self.pin_attempts += 1
                print(f"PIN attempts: {self.pin_attempts}/{self.max_attempts}")
                
                if self.pin_attempts >= self.max_attempts:
                    print("Guard: [attempts > 3]")
                    print("Action: Block card")
                    self.state = "Rejected"
                else:
                    self.state = "Authentication"  # Stay in the same state
            
            print("Exit Action: Verify PIN")
            print(f"Transition to: {self.state}")
            
        elif self.state == "MainMenu":
            if event == "Select Account Info":
                self.state = "AccountInfo"
                print(f"Transition to: {self.state}")
                print(f"Your current balance is: ${self.account_balance}")
                
            elif event == "Select Withdraw":
                self.state = "WithdrawMoney"
                print(f"Transition to: {self.state}")
                
            elif event == "Select Exit":
                print("Action: Eject card")
                self.state = "Idle"
                print(f"Transition to: {self.state}")
                
        elif self.state == "AccountInfo" and event == "Return":
            self.state = "MainMenu"
            print(f"Transition to: {self.state}")
            
        elif self.state == "WithdrawMoney":
            if event == "Select Back":
                self.state = "MainMenu"
                print(f"Transition to: {self.state}")
                
            elif event == "Enter Amount":
                amount = args[0]
                self.state = "ProcessWithdrawal"
                print(f"Withdrawal amount: ${amount}")
                print(f"Transition to: {self.state}")
                
                if amount <= self.account_balance:
                    print("Guard: [sufficient funds]")
                    print(f"Action: Deduct ${amount} from account")
                    self.account_balance -= amount
                    self.transaction_history.append(f"Withdrew ${amount}")
                    self.state = "DispenseCash"
                    print(f"Transition to: {self.state}")
                    print(f"Dispensing ${amount}...")
                    self.state = "CheckAccountStatus"
                    print(f"Transition to: {self.state}")
                    
                    if self.account_balance == 0:
                        print("Guard: [balance = 0]")
                        print("Action: Close account")
                        self.state = "AccountClosed"
                        print(f"Transition to: {self.state}")
                        print("Your account has been closed due to zero balance")
                        print("Action: Eject card")
                        self.state = "Idle"
                        print(f"Transition to: {self.state}")
                    else:
                        print("Guard: [balance > 0]")
                        print(f"Remaining balance: ${self.account_balance}")
                        self.state = "MainMenu"
                        print(f"Transition to: {self.state}")
                else:
                    print("Guard: [insufficient funds]")
                    self.state = "InsufficientFunds"
                    print(f"Transition to: {self.state}")
                    print(f"Insufficient funds. Available balance: ${self.account_balance}")
                    
        elif self.state == "InsufficientFunds" and event == "Acknowledge":
            self.state = "MainMenu"
            print(f"Transition to: {self.state}")
            
        elif self.state == "Rejected":
            print("Your card has been blocked due to too many incorrect PIN attempts")
            print("Please contact your bank for assistance")
            self.state = "Idle"
            print(f"Transition to: {self.state}")
            
        else:
            print(f"No transition defined for state '{self.state}' with event '{event}'")
        
        return self.state

def run_demo():
    """Run a demonstration of the ATM state machine"""
    print("===== ATM STATE MACHINE SIMULATION =====")
    atm = ATM()
    
    # Scenario 1: Successful authentication and withdrawal
    print("\n--- SCENARIO 1: SUCCESSFUL AUTHENTICATION AND WITHDRAWAL ---")
    atm.process_event("Insert Card")
    atm.process_event("Enter PIN", "1234")  # Correct PIN
    atm.process_event("Select Withdraw")
    atm.process_event("Enter Amount", 200)
    atm.process_event("Select Account Info")
    atm.process_event("Return")
    atm.process_event("Select Exit")
    
    # Scenario 2: Failed authentication
    print("\n--- SCENARIO 2: FAILED AUTHENTICATION ---")
    atm = ATM()  # Reset the ATM
    atm.process_event("Insert Card")
    atm.process_event("Enter PIN", "9999")  # Wrong PIN
    atm.process_event("Enter PIN", "8888")  # Wrong PIN
    atm.process_event("Enter PIN", "7777")  # Wrong PIN
    atm.process_event("Enter PIN", "6666")  # Too many attempts
    
    # Scenario 3: Insufficient funds
    print("\n--- SCENARIO 3: INSUFFICIENT FUNDS ---")
    atm = ATM()  # Reset the ATM
    atm.process_event("Insert Card")
    atm.process_event("Enter PIN", "1234")  # Correct PIN
    atm.process_event("Select Withdraw")
    atm.process_event("Enter Amount", 600)  # More than balance
    atm.process_event("Acknowledge")
    atm.process_event("Select Exit")
    
    # Scenario 4: Account closure due to zero balance
    print("\n--- SCENARIO 4: ACCOUNT CLOSURE DUE TO ZERO BALANCE ---")
    atm = ATM()  # Reset the ATM
    atm.process_event("Insert Card")
    atm.process_event("Enter PIN", "1234")  # Correct PIN
    atm.process_event("Select Withdraw")
    atm.process_event("Enter Amount", 500)  # Exactly the balance

if __name__ == "__main__":
    run_demo()