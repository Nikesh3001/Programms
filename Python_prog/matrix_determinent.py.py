import numpy as np

# Function to get matrix input from user
def get_matrix():
    n = int(input("Enter the order of the square matrix (e.g., 2 for 2x2): "))
    print(f"Enter the {n}x{n} matrix row by row:")
    matrix = []
    for i in range(n):
        row = list(map(float, input(f"Row {i+1}: ").split()))
        if len(row) != n:
            print("Error: Each row must have", n, "elements.")
            return None
        matrix.append(row)
    return np.array(matrix)

# Main function
def main():
    matrix = get_matrix()
    if matrix is None:
        return

    print("\nMatrix:")
    print(matrix)

    try:
        det = np.linalg.det(matrix)
        print(f"\nDeterminant of the matrix: {det:.2f}")
    except np.linalg.LinAlgError:
        print("Error: Cannot compute determinant.")

# Run the program
if __name__ == "__main__":
    main()
