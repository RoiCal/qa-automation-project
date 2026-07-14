from decimal import Decimal


def parse_money(money_text: str) -> Decimal:
    """Convert a formatted money string to a Decimal value."""
    cleaned_text = money_text.replace("$", "").replace(",", "")
    return Decimal(cleaned_text)
