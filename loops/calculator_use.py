import calculator

sum_result = calculator.add(10, 5)
product_result = calculator.multiply(4, 3)
tax = sum_result * calculator.TAX_RATE

print("Sum:", sum_result)
print("Product:", product_result)
print(f"Calculated Tax: ${tax:.2f}")