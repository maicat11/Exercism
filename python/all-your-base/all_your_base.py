def rebase(input_base, digits, output_base):

    if (input_base < 2) or (output_base < 2):
        raise ValueError("Base must be greater than one.")

    if (sum(n < 0 for n in digits) > 0) or (sum(n >= input_base for n in digits) > 0):
        raise ValueError("Digits must be zero or larger")

    base_ten = sum([n * input_base ** i for i, n in enumerate(digits[::-1])])
    output_digits = []

    while base_ten > 0:
        output_digits.append(base_ten % output_base)
        base_ten //= output_base
    return output_digits[::-1]