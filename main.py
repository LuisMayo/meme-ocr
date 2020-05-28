#!/usr/bin/env python2

import sys
from memeocr import MemeOCR

def main(argv):
    ocr = MemeOCR()
    txt = ocr.recognize('recoveredImg.png')

if __name__ == '__main__':
    main(sys.argv)

