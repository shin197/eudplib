import sys
import os

sys.path.insert(0, os.path.abspath('..\\'))

from eudplib import *

LoadMap('outputmap/basemap/basemap.scx')


@EUDFunc
def f1(a):
    ret = EUDVariable(0)
    if EUDIf()(a == 0):
        ret << 1234
    if EUDElse()():
        ret << 5678
    EUDEndIf()

    return ret


@EUDFunc
def f2(a):
    if EUDIf()(a == 0):
        EUDReturn(1234)
    if EUDElseIf()(a == 1):
        EUDReturn(5678)
    EUDEndIf()
    return 9012


@EUDFunc
def main():
    a, b = f1(0), f1(1)
    c, d, e = f2(0), f2(1), f2(2)
    DoActions([
        SetDeaths(0, SetTo, a, 0),
        SetDeaths(1, SetTo, b, 0),
        SetDeaths(2, SetTo, c, 0),
        SetDeaths(3, SetTo, d, 0),
        SetDeaths(4, SetTo, e, 0),
    ])


SaveMap('outputmap\\testmultret.scx', main)
