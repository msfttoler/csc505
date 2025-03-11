```mermaid
classDiagram
    class CheckWriter {
        -units: List[str]
        -teens: List[str]
        -tens: List[str]
        +convert_amount_to_words(amount: float) str
        +convert_dollars_to_words(dollars: int) str
        +convert_hundreds_to_words(number: int) str
        +test_check_writer() void
    }
    
    class NumberConverter {
        <<interface>>
        +convert_to_words(number: float) str
    }
    
    class AmountFormatter {
        <<interface>>
        +format_amount(dollars: str, cents: int) str
    }
    
    CheckWriter ..|> NumberConverter : implements
    CheckWriter ..|> AmountFormatter : implements