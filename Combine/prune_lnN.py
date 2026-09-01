#!/usr/bin/env python3
import sys
import os

def cap_value(val_str, min_val=0.5, max_val=2.0):
    """
    Caps symmetric and asymmetric lnN values.
    Returns a tuple: (new_string, is_capped_boolean)
    """
    if val_str == '-':
        return val_str, False

    is_capped = False
    try:
        if '/' in val_str:
            down, up = val_str.split('/')
            down_f = float(down)
            up_f = float(up)

            new_down = min(max(down_f, min_val), max_val)
            new_up = min(max(up_f, min_val), max_val)

            if new_down != down_f or new_up != up_f:
                is_capped = True

            return f"{new_down:g}/{new_up:g}", is_capped
        else:
            v = float(val_str)
            new_v = min(max(v, min_val), max_val)
            if new_v != v:
                is_capped = True
            return f"{new_v:g}", is_capped
    except ValueError:
        # If parsing fails, return original string
        return val_str, False

def process_datacard(filepath):
    if not os.path.exists(filepath):
        print(f"Error: File '{filepath}' not found.")
        return

    with open(filepath, 'r') as f:
        lines = f.readlines()

    bins = []
    processes = []
    modified = False

    print(f"\n--- Processing: {filepath} ---")

    with open(filepath, 'w') as f:
        for line in lines:
            parts = line.strip().split()
            if not parts:
                f.write(line)
                continue

            # Track the 'bin' row. We overwrite it so we always have the
            # last seen 'bin' row (which matches the columns of the rate block)
            if parts[0] == 'bin':
                # Only grab it if it's the long list of bins mapping to processes
                if len(parts) > 5:
                    bins = parts[1:]
                f.write(line)

            # Track the 'process' row that contains the string names (not IDs)
            elif parts[0] == 'process':
                try:
                    # If this is the integer ID row (e.g. 0, -1, 1), it will parse as float
                    float(parts[1])
                except ValueError:
                    # It failed to parse as a number, so it must be the process names row
                    processes = parts[1:]
                f.write(line)

            # Identify lnN systematic lines
            elif len(parts) > 2 and parts[1] == 'lnN':
                name = parts[0]
                syst_type = parts[1]
                vals = parts[2:]

                new_vals = []
                for i, val in enumerate(vals):
                    new_val, capped = cap_value(val)
                    if capped:
                        proc_name = processes[i] if i < len(processes) else "UnknownProcess"
                        bin_name = bins[i] if i < len(bins) else "UnknownBin"
                        print(f"[Pruned] Syst: {name:<30} | Bin: {bin_name:<25} | Process: {proc_name:<30} | {val:<12} -> {new_val}")
                        modified = True
                    new_vals.append(new_val)

                # Reconstruct the line with fixed widths to maintain readability
                new_line = f"{name:<45} {syst_type:<5} " + " ".join(f"{v:<32}" for v in new_vals) + "\n"
                f.write(new_line)

            else:
                # Write non-lnN lines exactly as they were
                f.write(line)

    if modified:
        print(f"-> Successfully updated: {filepath}")
    else:
        print(f"-> No unphysical lnN values found. File unchanged.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: python {sys.argv[0]} <datacard1.txt> [datacard2.txt ...]")
        sys.exit(1)

    for datacard in sys.argv[1:]:
        process_datacard(datacard)
