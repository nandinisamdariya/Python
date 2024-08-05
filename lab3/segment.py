def print_8_segment(n):
    segments = [
        [" _ ", "| |", "|_|"],
        ["   ", "  |", "  |"],
        [" _ ", " _|", "|_ "],
        [" _ ", " _|", " _|"],
        ["   ", "|_|", "  |"],
        [" _ ", "|_ ", " _|"],
        [" _ ", "|_ ", "|_|"],
        [" _ ", "  |", "  |"],
        [" _ ", "|_|", "|_|"],
        [" _ ", "|_|", " _|"]
    ]
    for row in range(3):
        for digit in str(n):
            print(segments[int(digit)][row], end=" ")
        print()

n = int(input("Enter a number: "))
print_8_segment(n)
