# ~# !/usr/bin/env python
# ~# -*- coding: UTF-8 -*-
# ~# Test générateur + bricole

from threading import Thread as threading_Thread
from datetime import datetime
from time import sleep as time_sleep
from itertools import product as itertools_product
from sys import (
    stdout as sys_stdout,
    argv as sys_argv,
    exc_info as sys_exc_info,
    )
from string import (
    # ~# ascii_lowercase as string_ascii_lowercase,
    ascii_letters as string_ascii_letters,
    digits as string_digits,
    punctuation as string_punctuation,
    )


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    INVERTED = '\033[7m'


class stdoutControl:
    """
    VT100 Control Codes :
    http://www.termsys.demon.co.uk/vtansi.htm#cursor
    """
    ASCII_CR = '\r'
    ASCII_LF = '\n'
    CURSOR_UP_ONE = '\x1b[1A'
    ERASE_LINE = '\r\x1b[2K'


class msg:
    CONFIG_HEADER = '%s%s%s' % (
        bcolors.HEADER+bcolors.BOLD, '=> Config :\n', bcolors.ENDC)
    START = '%s%s%s' % (
        bcolors.OKBLUE+bcolors.BOLD, '=> Start : \n', bcolors.ENDC)
    SUCCESS = '%s%s%s' % (
        bcolors.OKGREEN+bcolors.BOLD, '\n=> SUCCESS\n', bcolors.ENDC)


class loop:
    LOOP = 0


class flashMsg(object):
    """
    http://sebastiandahlgren.se/2014/06/27/running-a-method-as-a-background-thread-in-python/
    """
    def __init__(self):
        thread = threading_Thread(target=self.processing)
        thread.daemon = True
        thread.start()

    def processing(combiPred):
        while True:
            sys_stdout.write('%s' % (
                stdoutControl.ERASE_LINE +
                '   ' +
                bcolors.OKBLUE +
                'Processing' +
                bcolors.ENDC))
            time_sleep(0.5)
            sys_stdout.flush()
            sys_stdout.write('%s' % (
                stdoutControl.ERASE_LINE +
                '   ' +
                bcolors.OKBLUE +
                bcolors.INVERTED +
                'Processing' +
                bcolors.ENDC))
            time_sleep(0.5)
            sys_stdout.flush()


def combi_prediction(chain, stringMaxLen):
    combiMax = 0
    for x in xrange(stringMaxLen):
        combiMax += len(chain)**(x+1)
    return combiMax


def generate_combination(chain, stringMaxLen):
    for x in xrange(stringMaxLen):
        for i in itertools_product(chain, repeat=x+1):
            if i == chain[-1]*(x+1):
                pass
            else:
                yield ''.join(i)


def write_word_list(chain, stringMaxLen):
    now = datetime.strftime(datetime.now(), '%Y-%m-%d_%H-%M-%S')
    # ~# with open('./wordlist.txt', 'wb') as f:
    with open('./%s_wordlist.txt' % (now), 'wb') as f:
        wordlist = generate_combination(chain, stringMaxLen)
        while wordlist != chain[-1]*(stringMaxLen):
            try:
                lineGen = wordlist.next()
                f.write('%s\n' % (lineGen))
                loop.LOOP += 1
            except StopIteration:
                return


# ~# chain = string_ascii_lowercase
chain = '%s%s%s' % (string_ascii_letters, string_digits, string_punctuation)
combiPred = combi_prediction(chain, int(sys_argv[1]))
sys_stdout.write(msg.CONFIG_HEADER)
sys_stdout.write('   Chain Char : %s\n' % (
    bcolors.WARNING+bcolors.BOLD+chain+bcolors.ENDC))
sys_stdout.write('   len Chain Char : %s\n' % (
    bcolors.WARNING+bcolors.BOLD+str(len(chain))+bcolors.ENDC))
sys_stdout.write('   Lengh combinations: %s\n' % (
    bcolors.WARNING+bcolors.BOLD+str(sys_argv[1])+bcolors.ENDC))
sys_stdout.write('   Max combinations : %s\n' % (
    bcolors.FAIL+bcolors.BOLD+str(combiPred)+bcolors.ENDC))
sys_stdout.write(msg.START)

kikooLolMsg = flashMsg()
write_word_list(chain, int(sys_argv[1]))
