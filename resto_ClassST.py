class restaurant:
    # Initializer with 2 parameters
    # With 4 hidden attributes inside of the constructor function
    def __init__(self, FoodName, FoodAmount):
        self._FoodName = FoodName
        self._FoodAmount = FoodAmount
        self._standard_price_per_pound = 0.00  # Private attribute
        self._calculated_price = 0.00  # Public attribute
        self.PriceList()

    def PriceList(self):
        if self._FoodName == 'Dry Cured Iberian Ham':
            self._standard_price_per_pound = 177.80
        elif self._FoodName == 'Wagyu Steaks':
            self._standard_price_per_pound = 450.00
        # Add other items similarly

    def _calculate_price(self):
        self._calculated_price = self._FoodAmount * self._standard_price_per_pound
        return self._calculated_price

    def get_FoodName(self):
        return self._FoodName

    def get_FoodAmount(self):
        return self._FoodAmount

    def get_standard_price(self):
        return self._standard_price_per_pound

    def getPrice_ST(self):
        return self._calculate_price()  # Corrected method call

    def __str__(self):
        return f"item: {self._FoodName}\n" \
               f"Amount ordered: {self._FoodAmount} pounds\n" \
               f"Price per pound: {self._standard_price_per_pound}\n" \
               f"Price per order: {self._calculated_price}\n"
