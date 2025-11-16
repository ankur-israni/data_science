def convert_int_to_string(int_value):
    return str(int_value)


def convert_float_to_string(float_value):
    return str(float_value)


def convert_int_to_float(int_value):
    return float(int_value)


def convert_str_to_float(str_value):
    return float(str_value)


def convert_float_to_int(float_value):
    return int(float_value)


def convert_str_to_int(str_value):
    return int(str_value)


# Execution
print("int to string conversion = ", convert_int_to_string(10))

print("float to string conversion = ", convert_float_to_string(10.99))

print("int to float conversion = ", convert_int_to_float(10))

print("str to float conversion = ", convert_str_to_float('10'))

print("float to int conversion = ", convert_float_to_int(10.99))

print("str to int conversion = ", convert_str_to_int('10'))
