# Assignment 8: File Handling
# Read data from input file, count lines,
# extract first two lines, and write them into a new file.

def process_file(input_file, output_file):
    try:
        # Open the input file in read mode
        with open(input_file, "r") as infile:
            lines = infile.readlines()   # Read all lines into a list

            # Count total lines
            line_count = len(lines)
            print(f"Total number of lines in {input_file}: {line_count}")

            # Extract first two lines (if available)
            extracted_lines = lines[:2]

        # Write extracted lines into a new file
        with open(output_file, "w") as outfile:
            outfile.writelines(extracted_lines)

        print(f"First two lines written into {output_file}")

    except FileNotFoundError:
        print(f"Error: The file {input_file} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage
process_file("input.txt", "output.txt")
