def transform(legacy_data):
    new_data = {}
    for point_val, letters in legacy_data.items():
        for letter in letters:
            new_data[letter.lower()] = point_val
    return new_data
