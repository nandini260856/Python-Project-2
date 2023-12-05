# FieldInhabitant.py

class FieldInhabitant:
    def __init__(self, symbol):
        self._symbol = symbol  # Protected member variable

    # Getter for symbol
    def get_symbol(self):
        return self._symbol

    # Setter for symbol
    def set_symbol(self, value):
        self._symbol = value
