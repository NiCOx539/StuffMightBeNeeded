"""
Usuage: 
        python3 "X:\Path\to\directory"
"""

import fileinput

import os
import sys

if os.name == 'nt':
    sep = "\\"
else:
    sep = "/"

j = 0
for dof in [x for x in os.walk(sys.argv[1])]:
    i = 0
    for filename in dof[2]:
        if filename[-5:] == ".html":
            FilePath = str(dof[0]) + sep + str(filename)
            if "HTTrack" in str(open(FilePath, "r").read()):
                with fileinput.FileInput(FilePath, inplace=True, backup='.bak') as file:
                    finalContent = ""
                    testContent = ""
                    OpenHttrackComment = False
                    for line in file:
                        for char in line:
                            if OpenHttrackComment:
                                if testContent[-3:] == "-->":
                                    OpenHttrackComment = False
                                pass
                            else:
                                if testContent[-13:] == "<!-- Mirrored":
                                    OpenHttrackComment = True
                            if not OpenHttrackComment:
                                finalContent += char
                            testContent += char

                with open(FilePath, "w") as f:
                    f.write(finalContent.replace("<!-- Mirrored", "").replace("<!-- Added by HTTrack -->", "").replace("<!-- /Added by HTTrack -->", ""))
