def justify_paragraph(paragraph, page_width):
    words = paragraph.split()
    current_line = []
    justified_lines = []

    for word in words:
        if len(' '.join(current_line + [word])) <= page_width:
            current_line.append(word)
        else:
            line = ' '.join(current_line)
            justified_lines.append(line.ljust(page_width))
            current_line = [word]

    # Handling the last line
    if current_line:
        line = ' '.join(current_line)
        justified_lines.append(line.ljust(page_width))

    return justified_lines

def get_user_input():
    paragraph = input("Enter the paragraph: ")
    while not paragraph:
        print("Paragraph cannot be empty. Please enter a valid paragraph.")
        paragraph = input("Enter the paragraph: ")

    page_width = input("Enter the page width: ")
    while not page_width.isdigit() or int(page_width) <= 0:
        print("Page width must be a positive integer. Please enter a valid page width.")
        page_width = input("Enter the page width: ")

    return paragraph, int(page_width)

def main():
    # Get user input
    paragraph_input, page_width_input = get_user_input()

    # Justify the paragraph
    justified_lines_output = justify_paragraph(paragraph_input, page_width_input)

    # Print the justified lines with array index
    for i, line in enumerate(justified_lines_output):
        print(f"[{i}] {line}")

if __name__ == "__main__":
    main()