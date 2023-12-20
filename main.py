class MultiplesOfThreeAndFive:
    def __init__(self, start=1, end=101):
        self.start = start
        self.end = end
        
    def print_numbers(self):
        for num in range(self.start, self.end):
            result = self.check_conditions(num)
            print(result)
            
    def check_conditions(self, num):
        div_by_3 = num % 3 == 0
        div_by_5 = num % 5 == 0
        var_to_return = ""

        if div_by_3:
            var_to_return = "Three"
        if div_by_5:
            var_to_return += "Five"
        if not div_by_3 and not div_by_5:
            var_to_return = str(num)
            
        return var_to_return

# Create an instance of the NumberPrinter class
number_printer = MultiplesOfThreeAndFive()

# Call the print_numbers method to print the numbers based on conditions
number_printer.print_numbers()