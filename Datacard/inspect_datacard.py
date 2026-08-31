#!/usr/bin/env python
"""
Standalone script: open a workspace ROOT file, get the RooWorkspace,
fetch a named RooDataSet, and print its contents.

Usage:
  python inspect_dataset.py <root_file> <workspace_name> <dataset_name>

Example (matches the failing case in the log):
  python inspect_dataset.py \
      /eos/home-k/kpal/tprime-hdna/finalSelection18p6-UL17/TprimeM700Decay5pct/ws/output_M125_GG2H.root \
      cms_hgg_13TeV \
      ggh_125_13TeV_Leptonic

NOTE on PyROOT null checks:
  f.Get(name) for a missing key does NOT return Python None.
  It returns a null-pointer proxy object that is truthy-False but not
  identical to None. So checks must use `if not obj:` NOT `if obj is None:`.
  This script uses `if not obj:` consistently for that reason.
"""

import sys
import ROOT

def main():
    if len(sys.argv) != 4:
        print("Usage: python inspect_dataset.py <root_file> <workspace_name> <dataset_name>")
        sys.exit(1)

    fpath, wsname, dsname = sys.argv[1], sys.argv[2], sys.argv[3]

    print(" --> [INFO] Opening file: %s" % fpath)
    f = ROOT.TFile.Open(fpath, "READ")

    if not f or f.IsZombie():
        print(" --> [ERROR] Could not open file, or file is zombie.")
        sys.exit(1)
    print(" --> [INFO] File opened OK. f.IsOpen():", f.IsOpen())

    # List top-level keys in the file, just to sanity check contents
    print(" --> [INFO] Top-level keys in file:")
    for key in f.GetListOfKeys():
        print("      -", key.GetName(), "[", key.GetClassName(), "] cycle:", key.GetCycle())

    # Try top level first
    ws = f.Get(wsname)

    # If not found at top level, look inside tagsDumper (standard flashgg/HiggsDNA layout)
    if not ws:
        print(" --> [INFO] Workspace not found at top level, trying inside 'tagsDumper' directory...")
        tdir = f.Get("tagsDumper")
        if not tdir:
            print(" --> [ERROR] 'tagsDumper' directory not found either.")
            f.Close()
            sys.exit(1)
        print(" --> [INFO] Contents of tagsDumper directory:")
        for key in tdir.GetListOfKeys():
            print("      -", key.GetName(), "[", key.GetClassName(), "] cycle:", key.GetCycle())
        ws = tdir.Get(wsname)

    if not ws:
        print(" --> [ERROR] Workspace '%s' not found (checked top level and tagsDumper)." % wsname)
        f.Close()
        sys.exit(1)
    print(" --> [INFO] Got workspace:", ws.GetName(), "class:", ws.ClassName())

    # List all datasets in the workspace, so we can see if dsname is even there
    # NOTE: ws.allData() returns a std::list<RooAbsData*> in modern ROOT,
    # which is directly iterable in Python (no .iterator()/.Next() needed).
    print(" --> [INFO] All datasets in workspace (ws.allData()):")
    all_data = ws.allData()
    found_names = []
    for d in all_data:
        found_names.append(d.GetName())
        n_entries = d.numEntries() if hasattr(d, "numEntries") else "n/a"
        print("      -", d.GetName(), "[", d.ClassName(), "] entries:", n_entries)

    if dsname not in found_names:
        print(" --> [WARNING] Requested dataset '%s' NOT found among ws.allData() names above!" % dsname)

    data = ws.data(dsname)
    if not data:
        print(" --> [ERROR] ws.data('%s') returned null." % dsname)
        f.Close()
        sys.exit(1)

    print(" --> [INFO] ws.data('%s') class:" % dsname, data.ClassName())
    print(" --> [INFO] numEntries():", data.numEntries())
    print(" --> [INFO] sumEntries():", data.sumEntries())

    argset = data.get()
    if not argset:
        print(" --> [ERROR] data.get() returned null (no RooArgSet).")
    else:
        names = [v.GetName() for v in argset]
        print(" --> [INFO] get() returned %d variables:" % len(names))
        for n in names:
            print("      -", n)
        if "weight_PileupUp" in names and "weight_PileupDown" in names:
            print(" --> [INFO] weight_PileupUp/Down: PRESENT")
        else:
            print(" --> [WARNING] weight_PileupUp/Down: MISSING")

    f.Close()
    print(" --> [INFO] Done.")

if __name__ == "__main__":
    main()
