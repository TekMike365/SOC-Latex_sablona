"""
            Generate .latexmkrc files

    Tento skritp vygeneruje .latexmkrc subory a
    je urceny pre tych co chcu pouzivat latexmk
    priamo v terminale.

    Ak pouzivate Visual Studio Code, tento subor
    ignorujte.
"""

# relativne cesty, v kt. bude .latexmkrc vygenerovany
PATHS = {
    ".",        # korenovy priecinok
    "kapitoly", # prieconok kapitoly
}

import sys
import os

clean = False
for arg in sys.argv[1:]:
    if arg in "--help":
        print("flags: --clean, --help")
        exit()
    elif arg in "--clean":
        clean = True

ROOT = os.path.dirname(__file__) + "/../"

if clean:
    print("cleaning .latexmkrc:")
    for path in PATHS:
        rcpath = ROOT + path + "/.latexmkrc"
        print(rcpath)
        try:
            os.remove(rcpath)
        except FileNotFoundError:
            print(f"ignoring file : not found")
else:
    print("generating .latexmkrc:")
    for path in PATHS:
        rcpath = ROOT + path + "/.latexmkrc"
        print(rcpath)
        with open(rcpath, "w") as f:
            f.write(f"$out_dir = \"{ROOT + path + '/build'}\"")

print("done.")

