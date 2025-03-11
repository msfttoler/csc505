```mermaid
classDiagram
    class ShoppingList {
        -listId: string
        -userId: string
        -items: Item[]
        +createList()
        +addItem()
        +removeItem()
        +updateItem()
    }
    
    class Item {
        -itemId: string
        -name: string
        -quantity: int
        -category: string
        -isChecked: boolean
        +updateQuantity()
        +toggleCheck()
    }
    
    class User {
        -userId: string
        -preferences: Object
        -lists: ShoppingList[]
        +createAccount()
        +login()
        +updatePreferences()
    }
    
    class LocalStorage {
        +saveData()
        +getData()
        +clearData()
    }

    User "1" -- "*" ShoppingList
    ShoppingList "1" -- "*" Item
    ShoppingList -- LocalStorage