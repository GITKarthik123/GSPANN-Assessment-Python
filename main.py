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

# Example Usage
paragraph_input = "This is a sample paragraph that we want to justify based on a given page width."
page_width_input = 20

justified_lines_output = justify_paragraph(paragraph_input, page_width_input)

# Print the justified lines with array index
for i, line in enumerate(justified_lines_output):
    print(f"Array [{i}] = {line}")
