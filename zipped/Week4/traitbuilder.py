from abc import ABC, abstractmethod
from typing import List

# Abstract Builder
class TraitBuilder(ABC):
    @abstractmethod
    def reset(self):
        pass
    
    @abstractmethod
    def build_trait(self):
        pass
    
    @abstractmethod
    def get_result(self):
        pass

# Concrete Builder for Developer Traits
class DeveloperTraitBuilder(TraitBuilder):
    def __init__(self):
        self.reset()
    
    def reset(self):
        self._trait = DeveloperTraits()
    
    def build_trait(self):
        self._trait.problem_solving = ProblemSolving()
        self._trait.continuous_learning = ContinuousLearning()
        self._trait.collaboration = Collaboration()
    
    def get_result(self):
        trait = self._trait
        self.reset()
        return trait

# Product
class DeveloperTraits:
    def __init__(self):
        self.problem_solving = None
        self.continuous_learning = None
        self.collaboration = None
        
    def display_traits(self) -> None:
        print("\nKey Developer Personality Traits:")
        print("\n1. Problem Solving")
        print("   - Analytical thinking")
        print("   - Creativity in solution design")
        print("   - Persistence in debugging")
        
        print("\n2. Continuous Learning")
        print("   - Natural curiosity")
        print("   - Adaptability to new technologies")
        print("   - Growth mindset")
        
        print("\n3. Collaboration")
        print("   - Effective communication")
        print("   - Empathy for team members and users")
        print("   - Reliability in commitments")

class ProblemSolving:
    def evaluate_problem(self) -> str:
        return "Analyzing problem context and constraints"
    
    def develop_solution(self) -> str:
        return "Developing and testing solutions"

class ContinuousLearning:
    def learn_new_tech(self) -> str:
        return "Learning new technologies and methodologies"
    
    def share_knowledge(self) -> str:
        return "Sharing knowledge with team members"

class Collaboration:
    def work_with_team(self) -> str:
        return "Working effectively with team members"
    
    def give_feedback(self) -> str:
        return "Providing constructive feedback"

# Director
class TraitDirector:
    def __init__(self, builder: TraitBuilder):
        self._builder = builder
    
    def construct_traits(self):
        self._builder.reset()
        self._builder.build_trait()

def main():
    # Create builder and director
    builder = DeveloperTraitBuilder()
    director = TraitDirector(builder)
    
    # Construct and display traits
    director.construct_traits()
    traits = builder.get_result()
    traits.display_traits()

if __name__ == "__main__":
    main()