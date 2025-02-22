#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Copyright (c) 2014 trgk

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""
from math import log2

from .. import core as c
from .. import utils as ut
from ..core.inplacecw import cpset, iand, ilshift, ior, irshift, iset, isub, ixor
from ..localize import _
from .memiof import f_dwadd_epd, f_dwread_epd, f_dwwrite_epd, f_setcurpl2cpcache


class EUDArrayData(c.EUDObject):
    """
    Structure for storing multiple values.
    """

    def __init__(self, arr):
        super().__init__()
        self.dontFlatten = True

        if isinstance(arr, int):
            arrlen = arr
            self._datas = [0] * arrlen
            self._arrlen = arrlen

        else:
            for i, item in enumerate(arr):
                ut.ep_assert(c.IsConstExpr(item), _("Invalid item #{}").format(i))
            self._datas = arr
            self._arrlen = len(arr)

    def GetDataSize(self):
        return self._arrlen * 4

    def WritePayload(self, buf):
        for item in self._datas:
            buf.WriteDword(item)

    # --------

    def GetArraySize(self):
        """Get size of array"""
        return self._arrlen


class EUDArray(ut.ExprProxy):
    def __init__(self, initval=None, *, _from=None):
        if _from is not None:
            dataObj = _from

        else:
            dataObj = EUDArrayData(initval)
            self.length = dataObj._arrlen

        super().__init__(dataObj)
        self._epd = ut.EPD(self)
        self.dontFlatten = True

    def get(self, key):
        return f_dwread_epd(self._epd + key)

    def __getitem__(self, key):
        return self.get(key)

    def set(self, key, item):
        return iset(self._epd, key, c.SetTo, item)

    def __setitem__(self, key, item):
        return self.set(key, item)

    def __iter__(self):
        raise EPError(_("Can't iterate EUDArray"))

    # in-place item operations
    # Total 6 cases = 3 × 2
    # [0, 1, 2] of (self._epd, key) are variable
    #  × val is variable or not
    def iadditem(self, key, val):
        return iset(self._epd, key, c.Add, val)

    # FIXME: add operator for f_dwsubtract_epd
    def isubtractitem(self, key, val):
        return iset(self._epd, key, c.Subtract, val)

    def isubitem(self, key, val):
        return isub(self._epd, key, val)

    # defined when val is power of 2
    def imulitem(self, key, val):
        if not isinstance(val, int):
            raise AttributeError
        if val == 0:
            return f_dwwrite_epd(self._epd + key, 0)
        # val is power of 2
        if val & (val - 1) == 0:
            return self.ilshiftitem(key, int(log2(val)))
        # val is negation of power of 2
        if -val & (-val - 1) == 0:
            pass
        raise AttributeError

    # defined when val is power of 2
    def ifloordivitem(self, key, val):
        if not isinstance(val, int):
            raise AttributeError
        if val == 0:
            raise ZeroDivisionError
        # val is power of 2
        if val & (val - 1) == 0:
            return self.irshiftitem(key, int(log2(val)))
        # val is negation of power of 2
        if -val & (-val - 1) == 0:
            pass
        raise AttributeError

    # defined when val is power of 2
    def imoditem(self, key, val):
        if not isinstance(val, int):
            raise AttributeError
        if val == 0:
            raise ZeroDivisionError
        # val is power of 2
        if val & (val - 1) == 0:
            return self.ianditem(key, val - 1)
        raise AttributeError

    # FIXME: merge logic with EUDVariable and VariableBase

    def ilshiftitem(self, key, val):
        if isinstance(val, int):
            return ilshift(self._epd, key, val)
        raise AttributeError

    def irshiftitem(self, key, val):
        if isinstance(val, int):
            return irshift(self._epd, key, val)
        raise AttributeError

    def ipowitem(self, key, val):
        if isinstance(val, int) and val == 1:
            return
        raise AttributeError

    def ianditem(self, key, val):
        iand(self._epd, key, val)

    def ioritem(self, key, val):
        ior(self._epd, key, val)

    def ixoritem(self, key, val):
        ixor(self._epd, key, val)

    # FIXME: Add operator?
    def iinvert(self, key):
        return self.ixoritem(key, 0xFFFFFFFF)

    def inot(self, key):
        raise AttributeError

    # item comparisons
    def eqitem(self, key, val):
        return c.MemoryEPD(self._epd + key, c.Exactly, val)

    def neitem(self, key, val):
        from .utilf import EUDNot

        return EUDNot(c.MemoryEPD(self._epd + key, c.Exactly, val))

    def leitem(self, key, val):
        return c.MemoryEPD(self._epd + key, c.AtMost, val)

    def geitem(self, key, val):
        return c.MemoryEPD(self._epd + key, c.AtLeast, val)

    def ltitem(self, key, val):
        from .utilf import EUDNot

        return EUDNot(c.MemoryEPD(self._epd + key, c.AtLeast, val))

    def gtitem(self, key, val):
        from .utilf import EUDNot

        return EUDNot(c.MemoryEPD(self._epd + key, c.AtMost, val))
