"""Product"""


class Product:
    """Represents product details."""

    def __init__(self, name="", price=0.0):
        """Initialise a product."""
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}: ${self.price:.2f}"


def test_product():
    product = Product("Laptop", 912.95)
    print(product)


if __name__ == '__main__':
    test_product()
