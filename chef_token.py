class token():
    def __init__(self, type: str, values: list):
        self.type = type
        self.values = values

    def __repr__(self):
        return str([self.type, self.values])

    def __str__(self):
        return ("Type = " + self.type + ". With value: " + self.values + '')