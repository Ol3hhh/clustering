source_file_path = r'D:\My\Pwr\SolVro\recrutation\Source\cocktail_dataset.txt'
output_file_path = 'D:/My/Pwr/SolVro/recrutation/Source/id.txt'

with open(source_file_path, 'r') as read_file, open(output_file_path, 'w') as write_file:
    line = read_file.read()  # Read the entire file content
    previous = None
    pprevious = None
    ppprevious = None
    capture = False  # This flag indicates whether we're in capture mode

    for current in line:
        if previous is not None and pprevious is not None and ppprevious is not None:
            # Check if the last four characters form the string 'id":'
            if (ppprevious + pprevious + previous + current) == 'id":':
                capture = True  # Start capturing the next characters
                continue

        # Start capturing symbols after 'id":'
        if capture:
            if current == ',':
                write_file.write('\n')
                capture = False  # Stop capturing when a comma is found
            else:
                write_file.write(current)  # Print the captured symbol without a newline

        # Update the characters for the next iteration
        ppprevious = pprevious
        pprevious = previous
        previous = current



