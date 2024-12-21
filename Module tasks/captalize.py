def capitalize_lines():
    print("Enter lines of text (type 'END' to stop):")
    lines = []
    
    while True:
        line = input()
        if line.strip().upper() == 'END' or line.strip().upper() == 'end':
            break
        lines.append(line.upper())

    for line in lines:
        print(line)

capitalize_lines()
