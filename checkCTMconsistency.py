# -*- coding: utf-8 -*-
'''
Script to check consistency of (manually created) ctm file
The script locates all mentions (named 'concepts' in the script) of one of the CONCEPT_TYPES and checks whether each of these concepts occurs twice. If a concept occurs only once, it should be checked and corrected manually.

NB: More than 2 mentions of a concept is not a problem.

Usage: python checkCTMconsistency.py <CTMfile>
'''

__author__ = "Kim Luyckx (luyckx.kim@gmail.com)"
__license__ = '''Copyright (C) 2014  Kim Luyckx <luyckx.kim@gmail.com>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program. If not, see <http://www.gnu.org/licenses/>.'''

import sys, re

GENERAL_TYPES = ["trial", "institution", "demographics"]
CONCEPT_TYPES = ["group", "cell", "lab", "report", "icd9cm", "medication"]

def errorCheck(CTMfile):
    print "Checking %s" %CTMfile
    
    with open(CTMfile, "r") as fi:
        lines = fi.read()
    conceptDict = findConceptTypes(lines)
    detectSingles(conceptDict)
    
def findConceptTypes(line):
    concepts=[]
    for CONCEPT_TYPE in CONCEPT_TYPES:
        result = re.findall(r'(%s:\w+)[)(;.,\t]?' %(CONCEPT_TYPE), line, re.IGNORECASE | re.DOTALL)
        if result != []:
            concepts.append(result)
    
    conceptDict={}
    for conceptgroup in concepts:
        for concept in conceptgroup:
            try:
                conceptDict[concept]+=1
            except:
                conceptDict[concept]=1
    return conceptDict

def detectSingles(conceptDict):
    for k,v in conceptDict.iteritems():
        if v == 1: print "SINGLE mention of concept: %s" %k
    print "Done checking"

if __name__ == "__main__":
    if sys.argv[1:]:
        CTMfile = sys.argv[1]
        errorCheck(CTMfile)
    else:
        print "missing CTM file argument"
