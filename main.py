from resolver import Resolver

def get_input(message, length):
    values = [] 
    for i in range(length):
        value = int(input(f"{message} {i + 1}:\n"))
        values.append(value)
    return values


def main():
    length = int(input("Insert how many modalities you want to use:\n"))
    xs = get_input("Insert the modality:", length)
    
    resolver = Resolver(xs)

    print(f"Mean: {resolver.compute_mean()}")
    print(f"Absolute frequencies: {resolver.get_absolute_frequencies()}")
    print(f"Relative frequencies: {resolver.get_relative_frequencies()}")


if __name__ == '__main__':
    main()