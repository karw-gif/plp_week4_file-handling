def read_and_modify_file(input_filename, output_filename):
    try:
        # Open the input file for reading
        with open(input_filename, 'r') as file:
            content = file.read()

        # Modify the content (for demonstration, we'll convert text to uppercase)
        modified_content = content.upper()

        # Write the modified content to a new output file
        with open(output_filename, 'w') as file:
            file.write(modified_content)

        print(f"File has been successfully modified and saved as {output_filename}")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except IOError:
        print(f"Error: The file '{input_filename}' could not be read.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    # Ask the user for an input filename and output filename
    input_filename = input("Please enter the input filename: ")
    output_filename = input("Please enter the output filename: ")

    # Call the function to read, modify, and write the file
    read_and_modify_file(input_filename, output_filename)

if __name__ == "__main__":
    main()
