import csv

def process_sequence(sequence):
    # Extract the 16th to 24th values (1-indexed, so 16 to 24 is 15 to 23 in 0-indexed lists)
    extracted_values = sequence[15:23]
    print(extracted_values)
    # Apply mod 26 and convert to letters with z = 0, a = 1, ..., x = 25
    letters = [(chr((num % 26) + ord('a') - 1) if num % 26 != 0 else 'z') for num in extracted_values]
    return ''.join(letters)

def main():
    # Open the input file and output file
    with open('sequences.csv', 'r') as infile, open('desequence.csv', 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        
        # Process each line in sequences.csv
        for row in reader:
            # Convert string values to integers
            sequence = list(map(int, row))
            # Process the sequence and convert to letters
            result = process_sequence(sequence)
            # Write the result to desequence.csv
            writer.writerow([result])

if __name__ == '__main__':
    main()
