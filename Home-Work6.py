class Calculator:

    def divide(self, num_1, num_2):
        try:
            result = num_1 / num_2
            return result
        except ZeroDivisionError:
            return 'Ділити на 0 не можна.'
        except TypeError as error:
            return f'Так ділити не можна: {error}'
        except:
            return 'Щось пішло не так'
    
    def multiply(self, num_1, num_2):
        try:
            result = num_1 * num_2
            return result
        except TypeError as error:
            return f'Так множити не можна: {error}'
        except:
            return 'Щось пішло не так'
    
    def add(self, num_1, num_2):
        try:
            result = num_1 + num_2
            return result
        except TypeError as error:
            return f'Так додавати не можна: {error}'
        except:
            return 'Щось пішло не так'
    
    def subtract(self, num_1, num_2):
        try:
            result = num_1 - num_2
            return result
        except TypeError as error:
            return f'Так віднімати не можна: {error}'
        except:
            return 'Щось пішло не так'


calc = Calculator()

print("=== Ділення ===")
res_1 = calc.divide(10, 5)
print(res_1)

res_2 = calc.divide(10, 0)
print(res_2)

res_3 = calc.divide(10, "F")
print(res_3)

print("\n=== Множення ===")
res_4 = calc.multiply(5, 3)
print(res_4)

res_5 = calc.multiply(5, "F")
print(res_5)

res_6 = calc.multiply(2.5, 4)
print(res_6)

print("\n=== Додавання ===")
res_7 = calc.add(7, 3)
print(res_7)

res_8 = calc.add(7, "F")
print(res_8)

res_9 = calc.add(2.5, 3.7)
print(res_9)

print("\n=== Віднімання ===")
res_10 = calc.subtract(10, 4)
print(res_10)

res_11 = calc.subtract(10, "F")
print(res_11)

res_12 = calc.subtract(8.5, 2.3)
print(res_12)