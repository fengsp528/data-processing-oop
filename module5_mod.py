class NumberProcessor:
    def __init__(self):
        self.numbers = []

    def read_numbers(self, n):
        """Reads N numbers from the user."""
        self.numbers = []
        for i in range(n):
            num = int(input(f"Enter number {i + 1}: "))
            self.numbers.append(num)

    def search_number(self, x):
        """Searches for the number X and returns its 1-based index or -1 if not found."""
        try:
            index = self.numbers.index(x)
            return index + 1  # Convert to 1-based index
        except ValueError:
            return -1

    def __str__(self):
        return f"Numbers: {self.numbers}"
        
