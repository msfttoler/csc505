class PrototypePage:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = []

class PrototypeFlow:
    def __init__(self):
        self.pages = {}
        self.total_pages = 0
        
    def add_page(self, name, description):
        """Add a new page to the prototype"""
        self.pages[name] = PrototypePage(name, description)
        self.total_pages += 1
        
    def connect_pages(self, from_page, to_page):
        """Create a connection between pages"""
        if from_page in self.pages and to_page in self.pages:
            self.pages[from_page].connections.append(to_page)
            
    def print_prototype_info(self):
        """Print information about the prototype pages and flow"""
        print(f"\nPrototype Information:")
        print(f"Total Pages: {self.total_pages}\n")
        print("Pages and Their Flows:")
        
        for page_name, page in self.pages.items():
            print(f"\nPage: {page_name}")
            print(f"Description: {page.description}")
            if page.connections:
                print("Connects to:", " -> ".join(page.connections))
            else:
                print("No outgoing connections")

# Create the prototype flow
prototype = PrototypeFlow()

# Add pages with descriptions
prototype.add_page("Welcome", "Welcome screen with app logo and entry options")
prototype.add_page("Login", "User login form with email and password")
prototype.add_page("Register", "New user registration form")
prototype.add_page("ListOverview", "Dashboard showing all shopping lists")
prototype.add_page("CreateList", "Form to create a new shopping list")
prototype.add_page("ViewList", "Detailed view of a single shopping list")
prototype.add_page("EditList", "Interface for modifying list items")
prototype.add_page("AddItems", "Form to add new items to the list")

# Define page connections
prototype.connect_pages("Welcome", "Login")
prototype.connect_pages("Welcome", "Register")
prototype.connect_pages("Login", "ListOverview")
prototype.connect_pages("Register", "ListOverview")
prototype.connect_pages("ListOverview", "CreateList")
prototype.connect_pages("ListOverview", "ViewList")
prototype.connect_pages("CreateList", "EditList")
prototype.connect_pages("ViewList", "EditList")
prototype.connect_pages("EditList", "AddItems")
prototype.connect_pages("AddItems", "EditList")

# Print the prototype information
prototype.print_prototype_info()