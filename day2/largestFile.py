import os

def find_largest_file(directory):
    max_size = 0
    largest_file = None
    
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            
            if file_size > max_size:
                max_size = file_size
                largest_file = file_path
                
    return largest_file, max_size

directory_path = r"C:\Users\Chepuri Bharath"  # Replace with actual path
largest_file, size = find_largest_file(directory_path)
print(f"Largest file: {largest_file} ({size} bytes)")

