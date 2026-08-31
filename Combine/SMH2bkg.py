#!/usr/bin/env python3
"""
SMH2bkg.py

In a combine/flashgg-style datacard, the "process" block has two lines:
    process   <name1>  <name2>  ...
    process   <num1>   <num2>   ...

Convention: numbers <0  -> signal
            numbers >=0 -> background
Numbers must be IDENTICAL for the same physics process across different
bins/categories (e.g. Hadronic_22plus23 vs Leptonic_22plus23).

This script takes a list of process-name prefixes (default:
VH, ggH, qqH, tHq, ttH) and re-labels every column whose process name
starts with one of those prefixes to a new, non-negative integer.
- A distinct new number is assigned per distinct process name (so
  ggH_2022_hgg and ggH_2023_hgg get different numbers, but ggH_2022_hgg
  gets the SAME number in every bin/category it appears in).
- New numbers start above the current maximum non-negative number used
  in the card, so they never collide with existing backgrounds
  (e.g. bkg_mass=1).

Usage:
    python relabel_process.py input_datacard.txt output_datacard.txt \
        [--prefixes VH ggH qqH tHq ttH]

Only the "process" (numbers) line is modified; every other line
(including spacing) is left untouched.
"""

import argparse
import re
import sys


def find_block(lines):
    """Locate the 'bin' / 'process' (names) / 'process' (numbers) / 'rate' block."""
    names_idx = None
    for i, line in enumerate(lines):
        tokens = line.split()
        if tokens and tokens[0] == "process":
            # first 'process' line = names, must be followed by another 'process' line (numbers)
            if i + 1 < len(lines) and lines[i + 1].split() and lines[i + 1].split()[0] == "process":
                names_idx = i
                break
    if names_idx is None:
        sys.exit("ERROR: could not find the 'process' name/number block in the datacard.")

    numbers_idx = names_idx + 1
    bin_idx = names_idx - 1
    while bin_idx >= 0 and not (lines[bin_idx].split() and lines[bin_idx].split()[0] == "bin"):
        bin_idx -= 1
    if bin_idx < 0:
        sys.exit("ERROR: could not find the 'bin' line above the process block.")

    return bin_idx, names_idx, numbers_idx


def relabel(lines, prefixes):
    bin_idx, names_idx, numbers_idx = find_block(lines)

    bin_tokens = lines[bin_idx].split()[1:]
    name_tokens = lines[names_idx].split()[1:]

    if len(bin_tokens) != len(name_tokens):
        sys.exit("ERROR: 'bin' and 'process' (name) lines have different column counts.")

    # split the numbers line preserving whitespace so we can edit values in place
    parts = re.split(r"(\s+)", lines[numbers_idx].rstrip("\n"))
    # parts alternates: token, whitespace, token, whitespace, ...
    value_positions = [i for i, p in enumerate(parts) if p.strip() != ""]
    # first value token is the literal word 'process'
    value_positions = value_positions[1:]

    if len(value_positions) != len(name_tokens):
        sys.exit("ERROR: number of values in process-number line doesn't match process-name line.")

    old_numbers = [int(parts[pos]) for pos in value_positions]
    max_existing_nonneg = max([n for n in old_numbers if n >= 0], default=-1)

    # assign new numbers per distinct matching process name, in first-seen order
    next_number = max_existing_nonneg + 1
    name_to_new_number = {}
    for name in name_tokens:
        if any(name.startswith(p) for p in prefixes):
            if name not in name_to_new_number:
                name_to_new_number[name] = next_number
                next_number += 1

    changed = []
    for col, (name, pos) in enumerate(zip(name_tokens, value_positions)):
        if name in name_to_new_number:
            new_val = name_to_new_number[name]
            old_val = parts[pos]
            parts[pos] = str(new_val)
            changed.append((bin_tokens[col], name, old_val, new_val))

    lines[numbers_idx] = "".join(parts) + "\n"
    return lines, name_to_new_number, changed


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("input", help="path to input datacard")
    ap.add_argument("output", help="path to write modified datacard")
    ap.add_argument(
        "--prefixes",
        nargs="+",
        default=["VH", "ggH", "qqH", "tHq", "ttH"],
        help="process-name prefixes to relabel as background (default: VH ggH qqH tHq ttH)",
    )
    args = ap.parse_args()

    with open(args.input) as f:
        lines = f.readlines()

    lines, mapping, changed = relabel(lines, args.prefixes)

    with open(args.output, "w") as f:
        f.writelines(lines)

    print(f"Wrote {args.output}")
    print("\nNew process -> number mapping (identical across all bins/categories):")
    for name, num in mapping.items():
        print(f"  {name:35s} -> {num}")
    print(f"\nTotal columns changed: {len(changed)}")


if __name__ == "__main__":
    main()
