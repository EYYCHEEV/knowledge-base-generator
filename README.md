
# Markdown-based Knowledge Base Generator

This script is designed to consolidate various code and documentation files into a single, markdown-based knowledge base with support for syntax highlighting. It searches for files of specified types within a given Git repository directory, combining them into one or more markdown files, chunked by a maximum character count to ensure manageability.

## Features

- **Git Repository Support**: Accepts a Git repository path as input to search for files.
- **Recursive File Search**: Recursively finds files of specified types in the given directory.
- **Syntax Highlighting**: Adds markdown syntax highlighting for various programming languages.
- **Chunking**: Splits content into multiple files if the character limit is exceeded, keeping files manageable.
- **Customizable**: Allows customization of file types to search for and the maximum character count per file.

## Requirements

- Python 3.6 or later

## Usage

1. **Set Up Your Environment**: Ensure Python 3.6 or later is installed on your system.
2. **Run the Script**:
   - To specify custom paths:
     ```
     python knowledge_base_gen.py <repo_path> -o <output_directory>
     ```
     - `<repo_path>`: Path to the Git repository where the script will be executed.
     - `<output_directory>`: Path where the output files will be saved. If `-o` is not specified, the current directory will be used.
   - To use the script's location as both the source and output directory, simply run without any arguments:
     ```
     python knowledge_base_gen.py
     ```
     If no arguments are provided, the script will use the script file's location for both the repository path and the output directory.

## Arguments

- `repo_path`: Required. The path to the Git repository to process.
- `-o`, `--output`: Optional. Specifies the output directory path where the markdown files will be saved. Defaults to the current directory.

## Supported File Types

The script is configured to search for and include the following file types:
- Markdown (md)
- JavaScript (js, jsx)
- TypeScript (ts, tsx)
- Java (java)
- Go (go)
- Rust (rs)
- Swift (swift)
- Kotlin (kt)
- C# (cs)
- C (c)
- C++ (cpp)
- Python (py)
- Lua (lua)
- Luau (luau)

You can easily add or remove file types by editing the `file_types` list in the script.

## Contributing

Feel free to fork the repository, make improvements, and submit pull requests. Your contributions help make this tool more versatile and useful!

## License

This script is released under the MIT License. See the LICENSE file in the repository for more information.
