import numpy as np
import sys
import ROOT

try:
    file_name = sys.argv[1]
    file_ = ROOT.TFile.Open(file_name, "READ")

    if not file_ or file_.IsZombie():
        print(f"Error: Could not open {file_name}", file=sys.stderr)
        sys.exit(2)

    tree_ = file_.Get("limit")
    if not tree_:
        print(f"Error: Could not find 'limit' tree in {file_name}", file=sys.stderr)
        sys.exit(3)

    tree_.SetBranchStatus("*", 1)
    qlimit = np.zeros(1, dtype=np.float64)
    tree_.SetBranchAddress("limit", qlimit)

    limitVal = []
    for ievent in range(tree_.GetEntries()):
        tree_.GetEntry(ievent)
        limitVal.append(qlimit[0])

    file_.Close()

    print(limitVal)
    if len(limitVal) == 6:
        sys.exit(0)
    else:
        print(f"Unexpected number of entries: {len(limitVal)}", file=sys.stderr)
        sys.exit(4)

except Exception as e:
    print(f"Unexpected error: {e}", file=sys.stderr)
    sys.exit(101)
