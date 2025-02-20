# Level 1 - Highest level abstraction
def convert_amount_to_words(amount):
    """
    Convert a numeric dollar amount to words as would appear on a check.
    Example: 1234.56 -> "ONE THOUSAND TWO HUNDRED THIRTY-FOUR AND 56/100"
    """
    dollars = int(amount)
    cents = int(round((amount - dollars) * 100))
    return f"{convert_dollars_to_words(dollars)} AND {cents:02d}/100"

# Level 2 - Breaking down the dollar conversion
def convert_dollars_to_words(dollars):
    """
    Convert the dollar portion to words, handling different magnitude ranges.
    """
    if dollars == 0:
        return "ZERO"
    
    # Break into groups of thousands
    billions = dollars // 1000000000
    millions = (dollars % 1000000000) // 1000000
    thousands = (dollars % 1000000) // 1000
    remainder = dollars % 1000
    
    result = []
    
    if billions:
        result.append(f"{convert_hundreds_to_words(billions)} BILLION")
    if millions:
        result.append(f"{convert_hundreds_to_words(millions)} MILLION")
    if thousands:
        result.append(f"{convert_hundreds_to_words(thousands)} THOUSAND")
    if remainder or not result:
        result.append(convert_hundreds_to_words(remainder))
    
    return " ".join(result)

# Level 3 - Detailed conversion of numbers to words
def convert_hundreds_to_words(number):
    """
    Convert a number less than 1000 to words.
    """
    units = ["", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
    teens = ["TEN", "ELEVEN", "TWELVE", "THIRTEEN", "FOURTEEN", "FIFTEEN", 
             "SIXTEEN", "SEVENTEEN", "EIGHTEEN", "NINETEEN"]
    tens = ["", "", "TWENTY", "THIRTY", "FORTY", "FIFTY", "SIXTY", "SEVENTY", 
            "EIGHTY", "NINETY"]
    
    if number == 0:
        return ""
        
    result = []
    
    # Handle hundreds
    if number >= 100:
        result.append(f"{units[number // 100]} HUNDRED")
        number %= 100
        
    # Handle tens and ones
    if number >= 20:
        ten_word = tens[number // 10]
        one_word = units[number % 10]
        if one_word:
            result.append(f"{ten_word}-{one_word}")
        else:
            result.append(ten_word)
    elif number >= 10:
        result.append(teens[number - 10])
    elif number > 0:
        result.append(units[number])
        
    return " ".join(result)

# Example usage and testing
def test_check_writer():
    """
    Test the check writer with various amounts.
    """
    test_cases = [
        0.00,
        1.23,
        45.67,
        100.00,
        1234.56,
        1000000.00,
        1234567.89,
        1000000000.00
    ]
    
    for amount in test_cases:
        print(f"\nAmount: ${amount:.2f}")
        print(f"In words: {convert_amount_to_words(amount)}")

if __name__ == "__main__":
    test_check_writer()