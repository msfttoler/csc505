class TolerModel:
    def __init__(self):
        self.communication = None
        self.planning = None
        self.modeling = None
        self.construction = None
        self.deployment = None
        self.prototype_feedback = None
        self.user_checkpoints = None

    def get_inputs(self):
        print("=== Toler Model ===")
        self.communication = input("Enter the goals and requirements communicated by users: ")
        self.planning = input("Enter the planning elements (timelines, resources): ")
        self.modeling = input("Enter the design and architecture models: ")
        self.construction = input("Enter the key elements of construction (coding details): ")
        self.deployment = input("Enter the deployment strategy: ")
        self.prototype_feedback = input("Enter feedback collected during prototyping: ")
        self.user_checkpoints = input("Enter user involvement checkpoints: ")

    def display_model(self):
        print("\n=== Toler Model Outputs ===")
        print(f"1. Communication Phase: {self.communication}")
        print(f"2. Planning Phase: {self.planning}")
        print(f"3. Modeling Phase: {self.modeling}")
        print(f"4. Construction Phase: {self.construction}")
        print(f"5. Deployment Phase: {self.deployment}")
        print(f"6. Prototyping Feedback: {self.prototype_feedback}")
        print(f"7. User Checkpoints: {self.user_checkpoints}")


# Main Program
if __name__ == "__main__":
    model = TolerModel()
    model.get_inputs()
    model.display_model()