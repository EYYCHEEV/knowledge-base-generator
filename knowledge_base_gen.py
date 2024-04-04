import argparse
import glob
import os

def find_files(start_path, file_types):
    """Recursively find all files of specified types in the given directory."""
    files = []
    for file_type in file_types:
        files.extend(
            glob.glob(os.path.join(start_path, "**", f"*.{file_type}"), recursive=True)
        )
    return files

def combine_files_with_chunking(
    file_paths, output_file_base, output_dir, max_chars=1_200_000
):
    """Combine the content of all specified files into chunked files,
    based on a maximum character limit, including code files with syntax highlighting.
    """
    file_index = 1
    current_chars = 0
    output_file = os.path.join(output_dir, f"{output_file_base}-{file_index}.md")
    file_count = 0

    with open(output_file, "w", encoding="utf-8") as outfile:
        for file_path in file_paths:
            try:
                with open(file_path, "r", encoding="utf-8") as infile:
                    file_extension = file_path.split(".")[-1]
                    content = infile.read()
                    # Add syntax highlighting for markdown
                    if file_extension in file_types:
                        content = f"```{file_extension}\n{content}\n```\n"
                    # Include full path for code files
                    content = f"**File: {file_path}**\n\n{content}"
            except IOError as e:
                print(f"Could not read file {file_path}. Error: {e}")
                continue  # Skip to the next file

            content_len = len(content) + 2  # Adding 2 for the newline characters

            if current_chars + content_len > max_chars:
                file_index += 1
                output_file = os.path.join(
                    output_dir, f"{output_file_base}-{file_index}.md"
                )
                outfile = open(output_file, "w", encoding="utf-8")
                current_chars = 0
                print(f"Creating new output file: {output_file}")

            outfile.write(content + "\n\n")
            current_chars += content_len
            file_count += 1

    print(f"Files have been combined and chunked. {file_count} files processed.")

def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Combine files into a markdown-based knowledge base."
    )
    parser.add_argument(
        "repo_path",
        type=str,
        help="Path to the Git repository where the script will be executed"
    )
    parser.add_argument("-o", "--output", help="Output directory path", default=".")
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_arguments()
    repo_path = args.repo_path  # Use the provided repo_path from arguments
    working_dir_name = os.path.basename(os.path.normpath(repo_path))
    output_file_base = f"{working_dir_name}-knowledge-base"
    output_dir = args.output

    file_types = [
        "txt",
        "md",
        "js",
        "jsx",
        "ts",
        "tsx",
        "java",
        "go",
        "rs",
        "swift",
        "kt",
        "cs",
        "c",
        "cpp",
        "py",
        "lua",
        "luau",
    ]

    files = find_files(repo_path, file_types)
    combine_files_with_chunking(files, output_file_base, output_dir)
