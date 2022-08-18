"""Classes for melon orders."""
from itertools import count


class AbstractMelonOrder:
    """An abstract base class that other Melon Orders inherit from."""

    # the following 2 lines can be included, but are not necessary because 
    # AbstractMelonOrder should never be instantiated directly

    order_type = None
    tax = 0

    def __init__(self, species, qty, country_code=None):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.country_code = country_code

    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5

        if self.species == "christmas":
            base_price = base_price * 1.5

        total = (1 + self.tax) * self.qty * base_price

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    order_type = "domestic"
    tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    order_type = "international"
    tax = 0.17

    def get_total(self):
        """Check if order qty is less than 10 and add fee"""

        if self.qty < 10:
            total = super().get_total() + 3
        else:
            total = super().get_total()
        
        return total

    def get_country_code(self):
        """Return the country code."""

        return self.country_code


class GovernmentMelonOrder(AbstractMelonOrder):
    """A U.S. government melon order."""
    order_type = 'government'
    tax = 0
    passed_inspection = False

    def mark_inspection(self, passed):
    
        if passed == True:
            self.passed_inspection = True

"""
mylist.sorted()
print(mylist)

sort(mylist2)
print(mylist2)
mylist2_sorted = sorted(mylist2)
"""