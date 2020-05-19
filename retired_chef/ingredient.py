class Ingredient:
    """
    Dit is de classe waar alle waardes van een ingredient worden opgeslagen.
    """
    def __init__(self, amount: int, state: str, name: str):
        self.name = name
        self.amount = amount
        self.state = state

    def __str__(self):
        s = "Ingredient:" + str(self.name) +\
             " - amount:" + str(self.amount) +\
             " - state:" + str(self.state)
        if self.state == "liquid":
            s += " - current output: " + chr(self.amount)
        else:
            s += " - current output: " + str(self.amount)
        return s

    def get_name(self) -> str:
        return self.name

    def set_name(self, name) -> None:
        self.name = name

    def get_amount(self) -> int:
        return self.amount

    def set_amount(self, amount) -> None:
        self.amount = amount

    def get_state(self) -> str:
        return self.state

    def set_state(self, state) -> None:
        self.state = type

    def dry(self):
        self.state = "dry"

    def liquefy(self):
        self.state = "liquid"

    def serve(self):
        if self.state == "liquid":
            return chr(self.amount)
        return str(self.amount)
