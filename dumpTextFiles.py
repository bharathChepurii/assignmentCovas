import os

def dump_text_files(source_directory, output_file):
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for root, _, files in os.walk(source_directory):
            for file in files:
                if file.endswith('.txt'):  
                    file_path = os.path.join(root, file)
                    with open(file_path, 'r', encoding='utf-8') as infile:
                        outfile.write(f"\n------ {file} ------\n")  
                        outfile.write(infile.read())

source_dir = "your directory path here"  # Replace with actual path
output_file = "merged_output.txt"
dump_text_files(source_dir, output_file)
print(f"All text files have been merged into {output_file}")

