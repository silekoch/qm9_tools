#!/usr/bin/env python3
import sys
import os
import argparse


def simplify(input_file, output_file):
    """
    Simplify a single .xyz file from extended format to basic format.
    """
    try:
        with open(input_file, 'r') as infile:
            # Read the first line and get the number of atoms (n)
            n_atoms_line = infile.readline().strip()
            n_atoms = int(n_atoms_line)

            # Skip the second line
            infile.readline()

            # Read the next n lines containing atom data
            atom_lines = [infile.readline().strip() for _ in range(n_atoms)]

        output_lines = [n_atoms_line] + atom_lines

        # Write the simplified lines to the output file
        with open(output_file, 'w') as outfile:
            outfile.write('\n'.join(output_lines) + '\n')

        print(f"Processed {n_atoms} atoms: {input_file} -> {output_file}")
    except Exception as e:
        print(f"Error processing {input_file}: {e}")


def main():
    parser = argparse.ArgumentParser(
        description="Simplify QM9 .xyz files from extended format to basic format."
    )
    
    # Positional arguments for single-file mode:
    # 1) input_file (required if not using directory mode)
    # 2) output_file (optional, default <input_basename>-simplified.xyz)
    parser.add_argument(
        "input_file",
        nargs="?",
        help="Path to the single input .xyz file (positional). Required if not using directory mode."
    )
    parser.add_argument(
        "output_file",
        nargs="?",
        help="Path to the output .xyz file (positional). If omitted, defaults to <input_basename>-simplified.xyz."
    )

    # Optional arguments for directory mode
    parser.add_argument(
        "--input_dir", "-id",
        help="Path to a directory containing multiple .xyz files to be simplified."
    )
    parser.add_argument(
        "--output_dir", "-od",
        help="Path to a directory where the simplified .xyz files will be saved."
    )

    args = parser.parse_args()

    # Check if we are in directory mode
    if args.input_dir or args.output_dir:
        # We only proceed with directory mode if both --input_dir AND --output_dir are provided
        if not (args.input_dir and args.output_dir):
            parser.print_help()
            print("\nError: Both --input_dir and --output_dir must be provided for directory mode.")
            sys.exit(1)

        # Validate directory paths
        if not os.path.isdir(args.input_dir):
            print(f"Error: Input directory '{args.input_dir}' does not exist.")
            sys.exit(1)
        if not os.path.isdir(args.output_dir):
            print(f"Output directory '{args.output_dir}' does not exist. Creating it...")
            os.makedirs(args.output_dir, exist_ok=True)

        # Process all .xyz files in the input directory
        for file_name in os.listdir(args.input_dir):
            if file_name.lower().endswith(".xyz"):
                input_path = os.path.join(args.input_dir, file_name)
                output_path = os.path.join(args.output_dir, file_name)
                simplify(input_path, output_path)

    else:
        # Single-file mode
        if not args.input_file:
            parser.print_help()
            print("\nError: You must provide an input_file in single-file mode, "
                  "or use directory mode with --input_dir/--output_dir.")
            sys.exit(1)

        input_file = args.input_file

        # Check if the input file exists
        if not os.path.isfile(input_file):
            print(f"Error: The specified input file '{input_file}' does not exist. If you want to process a directory, please use --input_dir and --output_dir.")
            sys.exit(1)

        # Determine the output file
        if args.output_file:
            output_file = args.output_file
        else:
            # Default to <input_basename>-simplified.xyz
            base, ext = os.path.splitext(input_file)
            output_file = f"{base}-simplified.xyz"
        
        simplify(input_file, output_file)


if __name__ == "__main__":
    main()

