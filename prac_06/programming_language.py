class ProgrammingLanguage:
    """Request a ........."""

    def __init__(self, name, typing, reflection, year):
        """Initialise a lLanguage Instance"""

        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self) -> str:
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        return self.reflection == True
