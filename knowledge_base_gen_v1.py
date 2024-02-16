import os
import glob

def find_md_files(start_path):
    """Recursively find all markdown files in the given directory."""
    return glob.glob(os.path.join(start_path, '**', '*.md'), recursive=True)

def combine_md_files_with_chunking(file_paths, output_file_base, max_chars=1_200_000):
    """Combine the content of all markdown files into chunked files,
    based on a maximum character limit."""
    file_index = 1
    current_chars = 0
    output_file = f"{output_file_base}-{file_index}.md"
    file_count = 0

    with open(output_file, 'w', encoding='utf-8') as outfile:
        for file_path in file_paths:
            try:
                with open(file_path, 'r', encoding='utf-8') as infile:
                    content = infile.read()
            except IOError as e:
                print(f"Could not read file {file_path}. Error: {e}")
                continue  # Skip to the next file

            content_len = len(content) + 2  # Adding 2 for the newline characters

            # Check if adding this content would exceed the limit
            if current_chars + content_len > max_chars:
                # Close the current file and open a new one
                file_index += 1
                output_file = f"{output_file_base}-{file_index}.md"
                outfile = open(output_file, 'w', encoding='utf-8')
                current_chars = 0  # Reset character count for the new file
                print(f"Creating new output file: {output_file}")

            outfile.write(content + '\n\n')
            current_chars += content_len
            file_count += 1

    print(f"Markdown files have been combined and chunked. {file_count} files processed.")

if __name__ == "__main__":
    repo_path = '.'  # Assuming this script is run from the root of the repository
    output_file_base = 'roblox-knowledge-base'  # Base name for output files

    # Find all markdown files in the repository
    md_files = find_md_files(repo_path)

    # Combine all markdown files into chunked files
    combine_md_files_with_chunking(md_files, output_file_base)

    print("Process completed successfully.")
