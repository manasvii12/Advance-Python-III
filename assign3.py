# Strategy Interface
class PaymentStrategy:
    def pay(self, amount):
        raise NotImplementedError("Subclass must implement abstract method")


# Concrete Strategies
class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number):
        self.card_number = card_number

    def pay(self, amount):
        print(f"Paid {amount} using Credit Card [Card No: {self.card_number}]")


class PayPalPayment(PaymentStrategy):
    def __init__(self, email):
        self.email = email

    def pay(self, amount):
        print(f"Paid {amount} using PayPal [Email: {self.email}]")


class UPIPayment(PaymentStrategy):
    def __init__(self, upi_id):
        self.upi_id = upi_id

    def pay(self, amount):
        print(f"Paid {amount} using UPI [UPI ID: {self.upi_id}]")


# Context Class
class PaymentProcessor:
    def __init__(self, strategy: PaymentStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: PaymentStrategy):
        """Allows changing payment method at runtime"""
        self.strategy = strategy

    def process_payment(self, amount):
        self.strategy.pay(amount)


# Client Code
if __name__ == "__main__":
    # Using Credit Card
    processor = PaymentProcessor(CreditCardPayment("1234-5678-9876"))
    processor.process_payment(500)

    # Switching to PayPal
    processor.set_strategy(PayPalPayment("user@example.com"))
    processor.process_payment(750)

    # Switching to UPI
    processor.set_strategy(UPIPayment("manasvi@upi"))
    processor.process_payment(300)
