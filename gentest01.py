#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#from __future__ import unicode_literals

from itertools import product as itertools_product
from string import ascii_lowercase as string_ascii_lowercase
from datetime import datetime

chain = string_ascii_lowercase
stringMaxLen = 3
now = datetime.strftime(datetime.now(),'%Y-%m-%d_%H-%M-%S')


def genCombi(chain, stringMaxLen):
    for x in xrange(stringMaxLen):
        for i in itertools_product(chain, repeat = x+1):
            if i == chain[-1]*(x+1):
                pass
            else:
                yield ''.join(i)


with open('./%s_dico.txt' %(now), 'wb') as f:
    wordlist = genCombi(chain, stringMaxLen)
    while wordlist != chain[-1]*(stringMaxLen):
        f.write('%s\n' %(wordlist.next()))
