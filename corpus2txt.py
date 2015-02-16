#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Script to convert a corpus to text file
@author: Le Tuan Anh
'''

# Copyright (c) 2015, Le Tuan Anh <tuananh.ke@gmail.com>
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in
#all copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#THE SOFTWARE.

__author__ = "Le Tuan Anh"
__copyright__ = "Copyright 2015, OMWTK"
__credits__ = [ "Le Tuan Anh" ]
__license__ = "MIT"
__version__ = "0.1"
__maintainer__ = "Le Tuan Anh"
__email__ = "tuananh.ke@gmail.com"
__status__ = "Prototype"

########################################################################

import os
from puchikarui.puchikarui import Schema
from collections import namedtuple
from chirptext.leutile import Counter

########################################################################
# Configuration
########################################################################

NTUMC_DB_PATH=os.path.expanduser('./data/eng.db')
OUTPUT_FILE=os.path.expanduser('./data/eng.txt')
# Sense=namedtuple('SenseInfo', 'POS SenseID PosScore NegScore SynsetTerms Gloss'.split())

class NTUMCSchema(Schema):
	def __init__(self, data_source=None):
		Schema.__init__(self, data_source)
		self.add_table('sent', 'sid docID pid sent comment usrname'.split())

########################################################################

def main():
	print("Script to convert NTU-MC to text file")
	db = NTUMCSchema.connect(NTUMC_DB_PATH)
	sents = db.sent.select(where='sid >= ? and sid <= ?', values=[10000, 10999])
	with open(OUTPUT_FILE, 'w') as outfile: 
		for sent in sents:
			outfile.write(sent.sent)
			outfile.write('\n')
	print("Done!")
	pass

if __name__ == "__main__":
	main()
