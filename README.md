# QM9 Tools

A small collection of scripts and utilities for working with the QM9 dataset.

## Description

This repository contains tools to parse, simplify, and handle QM9 `.xyz` files. The main script, `simplify_qm9.py`, converts extended QM9 `.xyz` files into a simplified format by discarding extraneous data lines while retaining essential atom information.

## Usage

### Single-File Mode

By default, you can provide one or two positional arguments:
1. The input `.xyz` file (required).
2. The output `.xyz` file (optional; defaults to `<input_basename>-simplified.xyz`).

Example:
```bash
python simplify_qm9.py my_molecule.xyz
```
or
```bash
python simplify_qm9.py my_molecule.xyz my_output_simplified.xyz
```

### Directory Mode

You can also process an entire directory of `.xyz` files. Specify the input and output directories with `--input_dir` and `--output_dir`:

```bash
python simplify_qm9.py --input_dir path/to/xyz_files --output_dir path/to/simplified_files
```

## QM9 Paper

> **Raghunathan Ramakrishnan, Pavlo O. Dral, Matthias Rupp, O. Anatole von Lilienfeld.**  
> *Quantum chemistry structures and properties of 134 kilo molecules.*  
> Scientific Data (2014)

## License

This project is licensed under the [MIT License](LICENSE). See the [LICENSE](LICENSE) file for details.
