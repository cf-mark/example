for fizzbuzz in range(51):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("fizzbuzz")
        continue
    elif fizzbuzz % 3 == 0:
        print("fizz")
        continue
    elif fizzbuzz % 5 == 0:
        print("buzz")
        continue
    print(fizzbuzz)


class ExampleClass:

    def __init__(self, example):
        self.example = example


    def badMethodName():
        return example


exampel_class = ExampleClass('Heelo')

print(exampel_class.badMethodName())
