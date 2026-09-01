#!/usr/bin/env python3
import sys
import os

def cap_value(val_str, min_val=0.5, max_val=2.0):
    """Caps symmetric and asymmetric lnN values."""
    if val_str == '-':
        return val_str
    try:
        if '/' in val_str:
            down, up = val_str.split('/')
            down_f = min(max(float(down), min_val), max_val)
            up_f = min(max(float(up), min_val), max_val)
            # Use 'g' format to remove trailing zeros (e.g., 2.0 -> 2)
            return f"{down_f:g}/{up_f:g}"
        else:
            v = min(max(float(val_str), min_val), max_val)
            return f"{v:g}"
    except ValueError:
        # If parsing fails for some reason, return the original string
        return val_str

def process_datacard(filepath):
    if not os.path.exists(filepath):
        print(f"Error: File '{filepath}' not found.")
        return

    with open(filepath, 'r') as f:
        lines = f.readlines()

    modified = False
    with open(filepath, 'w') as f:
        for line in lines:
            parts = line.strip().split()
            # Identify lnN systematic lines (Name type val1 val2 ...)
            if len(parts) > 2 and parts[1] == 'lnN':
                name = parts[0]
                syst_type = parts[1]
                vals = parts[2:]

                # Cap the values
                new_vals = [cap_value(v) for v in vals]

                # Reconstruct the line with fixed widths to maintain readability
                # Using 45 chars for the name, 5 for 'lnN', and 32 for each value
                new_line = f"{name:<45} {syst_type:<5} " + " ".join(f"{v:<32}" for v in new_vals) + "\n"
                f.write(new_line)
                modified = True
            else:
                # Write non-lnN lines exactly as they were
                f.write(line)

    if modified:
        print(f"Successfully pruned and updated: {filepath}")
    else:
        print(f"No lnN systematics found/modified in: {filepath}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: python {sys.argv[0]} <datacard1.txt> [datacard2.txt ...]")
        sys.exit(1)

    for datacard in sys.argv[1:]:
        process_datacard(datacard)
