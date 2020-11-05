def greet_user():
    """Generic greeting for users"""
    print("Hello!")
    print("Welcome")

def greet_user_by_name(name, greeting):
    """Customized greeting"""
    print(greeting + " ," + name)


def cube(base_number):
    cubed_value = base_number * base_number * base_number
    return cubed_value


greet_user_by_name("Torrance", "Welcome")

eleven = cube(11)
print(eleven)