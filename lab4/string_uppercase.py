def capitalize_lines():
    lines = []
    while True:
        line = input("Enter a line: ")
        if not line:
            break
        lines.append(line.upper())
    
    for line in lines:
        print(line)

capitalize_lines()
