
from module5_oop import NumberProcessor

def main():
    processor = NumberProcessor()

    # Read input N
    n = int(input("Enter the number of elements (N): "))

    # Read N numbers
    processor.read_numbers(n)

    # Read input X
    x = int(input("Enter the number to search (X): "))

    # Search for X and print result
    result = processor.search_number(x)
    print(result)

if __name__ == "__main__":
    main()
