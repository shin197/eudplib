## NOTE: THIS FILE IS GENERATED BY EPSCRIPT! DO NOT MODITY
from eudplib import *
from eudplib.epscript.helper import _RELIMP, _IGVA, _CGFW, _ARR, _VARR, _SRET, _SV, _ATTW, _ARRW, _ATTC, _ARRC, _L2V, _LVAR, _LSH
# (Line 1) function square();
# (Line 3) const a = [
# (Line 4) square(1),
# (Line 5) square(2),
# (Line 6) square(3),
# (Line 7) square(4),
# (Line 8) square(5)
# (Line 9) ];
a = _CGFW(lambda: [_ARR(FlattenList([f_square(1), f_square(2), f_square(3), f_square(4), f_square(5)]))], 1)[0]
# (Line 11) function square(x) {
@EUDFunc
def f_square(x):
    # (Line 12) const z = EUDArray(5);
    z = EUDArray(5)
    # (Line 13) return x * x; // + z.k;
    EUDReturn(x * x)
    # (Line 14) }
    # (Line 15) const receives = py_eval('[PVariable() for _ in range(8)]');

receives = _CGFW(lambda: [eval('[PVariable() for _ in range(8)]')], 1)[0]
# (Line 16) const attack_gwpID = 4;
attack_gwpID = _CGFW(lambda: [4], 1)[0]
# (Line 17) function constv_thing() {
@EUDFunc
def f_constv_thing():
    # (Line 18) foreach(i, pvar: py_enumerate(receives)) {}
    for i, pvar in enumerate(receives):
        # (Line 19) SetMemoryXEPD(EPD(0x656FB8) + attack_gwpID/4, Add, 100 << (attack_gwpID%4 * 8), 0xFF << (attack_gwpID%4 * 8));  // cooldown +100
        pass

    # (Line 20) return a[0] + a[1] + a[2] + a[3] + a[4];
    DoActions(SetMemoryXEPD(EPD(0x656FB8) + attack_gwpID // 4, Add, _LSH(100,(attack_gwpID % 4 * 8)), _LSH(0xFF,(attack_gwpID % 4 * 8))))
    EUDReturn(a[0] + a[1] + a[2] + a[3] + a[4])
    # (Line 21) }
    # (Line 23) function switch_test(): EUDArray {

@EUDTypedFunc([], [EUDArray])
def f_switch_test():
    # (Line 24) const ret = EUDArray(6);
    ret = EUDArray(6)
    # (Line 25) static var x = 1234;
    x = EUDVariable(1234)
    # (Line 26) static var s = EPD(x.getValueAddr());
    s = EUDVariable(EPD(x.getValueAddr()))
    # (Line 28) switch(x) {}
    EUDSwitch(x)
    # (Line 29) epdswitch(s) {}
    EUDEndSwitch()
    EPDSwitch(s)
    # (Line 32) epdswitch (s, 240) {
    EUDEndSwitch()
    EPDSwitch(s, 240)
    # (Line 33) case 96:
    _t1 = EUDSwitchCase()
    # (Line 34) x += 1;
    if _t1(96):
        x.__iadd__(1)
        # (Line 35) break;
        EUDBreak()
        # (Line 36) case 160:
    _t2 = EUDSwitchCase()
    # (Line 37) x += 3;
    if _t2(160):
        x.__iadd__(3)
        # (Line 38) break;
        EUDBreak()
        # (Line 39) case 208:  // OK
    _t3 = EUDSwitchCase()
    # (Line 40) x += 5;
    if _t3(208):
        x.__iadd__(5)
        # (Line 41) break;
        EUDBreak()
        # (Line 42) default:
    # (Line 43) x = 0;
    if EUDSwitchDefault()():
        x << (0)
        # (Line 44) }
    # (Line 45) ret[0] = x;  // 1239
    EUDEndSwitch()
    _ARRW(ret, 0) << (x)
    # (Line 48) epdswitch (s, 56) {
    EPDSwitch(s, 56)
    # (Line 49) case 8:
    _t4 = EUDSwitchCase()
    # (Line 50) x += 2;
    if _t4(8):
        x.__iadd__(2)
        # (Line 51) break;
        EUDBreak()
        # (Line 52) case 16:  // OK
    _t5 = EUDSwitchCase()
    # (Line 53) x += 4;
    if _t5(16):
        x.__iadd__(4)
        # (Line 54) break;
        EUDBreak()
        # (Line 55) case 24:
    _t6 = EUDSwitchCase()
    # (Line 56) x += 6;
    if _t6(24):
        x.__iadd__(6)
        # (Line 57) break;
        EUDBreak()
        # (Line 58) case 32:
    _t7 = EUDSwitchCase()
    # (Line 59) x += 8;
    if _t7(32):
        x.__iadd__(8)
        # (Line 60) break;
        EUDBreak()
        # (Line 61) default:
    # (Line 62) x = 0;
    if EUDSwitchDefault()():
        x << (0)
        # (Line 63) }
    # (Line 64) ret[1] = x;  // 1243
    EUDEndSwitch()
    _ARRW(ret, 1) << (x)
    # (Line 67) switch (x, 432) {
    EUDSwitch(x, 432)
    # (Line 68) case 16:
    _t8 = EUDSwitchCase()
    # (Line 69) case 144:  // OK
    if _t8(16):
        pass
    _t9 = EUDSwitchCase()
    # (Line 70) x += 3;
    if _t9(144):
        x.__iadd__(3)
        # (Line 71) break;
        EUDBreak()
        # (Line 72) default:
    # (Line 73) x = 0;
    if EUDSwitchDefault()():
        x << (0)
        # (Line 74) }
    # (Line 75) ret[2] = x;  // 1246
    EUDEndSwitch()
    _ARRW(ret, 2) << (x)
    # (Line 78) switch (x, 211) {
    EUDSwitch(x, 211)
    # (Line 79) case 208:
    _t10 = EUDSwitchCase()
    # (Line 80) x += 5;
    if _t10(208):
        x.__iadd__(5)
        # (Line 81) break;
        EUDBreak()
        # (Line 82) case 210:
    _t11 = EUDSwitchCase()
    # (Line 83) x += 10;
    if _t11(210):
        x.__iadd__(10)
        # (Line 84) break;
        EUDBreak()
        # (Line 85) case 211:
    _t12 = EUDSwitchCase()
    # (Line 86) x += 15;
    if _t12(211):
        x.__iadd__(15)
        # (Line 87) break;
        EUDBreak()
        # (Line 88) default:
    # (Line 89) x = 0;
    if EUDSwitchDefault()():
        x << (0)
        # (Line 90) }
    # (Line 91) ret[3] = x;  // 1256
    EUDEndSwitch()
    _ARRW(ret, 3) << (x)
    # (Line 94) switch (x, 373) {
    EUDSwitch(x, 373)
    # (Line 95) case 96:  // OK
    _t13 = EUDSwitchCase()
    # (Line 96) x += 2;
    if _t13(96):
        x.__iadd__(2)
        # (Line 97) break;
        EUDBreak()
        # (Line 98) case 100:
    _t14 = EUDSwitchCase()
    # (Line 99) x += 5;
    if _t14(100):
        x.__iadd__(5)
        # (Line 100) break;
        EUDBreak()
        # (Line 101) case 112:
    _t15 = EUDSwitchCase()
    # (Line 102) x += 8;
    if _t15(112):
        x.__iadd__(8)
        # (Line 103) break;
        EUDBreak()
        # (Line 104) case 116:
    _t16 = EUDSwitchCase()
    # (Line 105) x += 11;
    if _t16(116):
        x.__iadd__(11)
        # (Line 106) break;
        EUDBreak()
        # (Line 107) default:
    # (Line 108) x = 0;
    if EUDSwitchDefault()():
        x << (0)
        # (Line 109) }
    # (Line 110) ret[4] = x;  // 1258
    EUDEndSwitch()
    _ARRW(ret, 4) << (x)
    # (Line 113) switch (x, 511) {
    EUDSwitch(x, 511)
    # (Line 114) case 121:
    _t17 = EUDSwitchCase()
    # (Line 115) x += 1;
    if _t17(121):
        x.__iadd__(1)
        # (Line 116) break;
        EUDBreak()
        # (Line 117) case 179:
    _t18 = EUDSwitchCase()
    # (Line 118) x += 4;
    if _t18(179):
        x.__iadd__(4)
        # (Line 119) break;
        EUDBreak()
        # (Line 120) case 234:  // OK
    _t19 = EUDSwitchCase()
    # (Line 121) x += 2;
    if _t19(234):
        x.__iadd__(2)
        # (Line 122) break;
        EUDBreak()
        # (Line 123) case 338:
    _t20 = EUDSwitchCase()
    # (Line 124) x += 8;
    if _t20(338):
        x.__iadd__(8)
        # (Line 125) break;
        EUDBreak()
        # (Line 126) case 428:
    _t21 = EUDSwitchCase()
    # (Line 127) x += 5;
    if _t21(428):
        x.__iadd__(5)
        # (Line 128) break;
        EUDBreak()
        # (Line 129) case 453:
    _t22 = EUDSwitchCase()
    # (Line 130) x += 7;
    if _t22(453):
        x.__iadd__(7)
        # (Line 131) break;
        EUDBreak()
        # (Line 132) default:
    # (Line 133) x = 0;
    if EUDSwitchDefault()():
        x << (0)
        # (Line 134) }
    # (Line 135) ret[5] = x;  // 1260
    EUDEndSwitch()
    _ARRW(ret, 5) << (x)
    # (Line 136) return ret;
    EUDReturn(ret)
    # (Line 137) }
    # (Line 139) const ack = PVariable(list(1, 2, 3, 4, 5, 6, 7, 8));

ack = _CGFW(lambda: [PVariable(FlattenList([1, 2, 3, 4, 5, 6, 7, 8]))], 1)[0]
# (Line 140) const ackMax = 8;
ackMax = _CGFW(lambda: [8], 1)[0]
# (Line 141) function test_array() {
@EUDFunc
def f_test_array():
    # (Line 142) var ret = 0;
    ret = _LVAR([0])
    # (Line 143) const p = EUDVariable(1);
    p = EUDVariable(1)
    # (Line 144) ret += ack[p] % ackMax > 4 ? 1 : 2;  // ret = 2
    ret.__iadd__(EUDTernary(ack[p] % ackMax <= 4, neg=True)(1)(2))
    # (Line 146) const arr = [1, 2, 3, 4, 5, 6, 7, 8];
    arr = _ARR(FlattenList([1, 2, 3, 4, 5, 6, 7, 8]))
    # (Line 147) ack[0] %= arr[p];
    _ARRW(ack, 0).__imod__(arr[p])
    # (Line 148) ret = ret >> 0;  // ret = 2
    ret << (ret >> 0)
    # (Line 150) ack[p] &= 1;  // ack[1] = 0
    _ARRW(ack, p).__iand__(1)
    # (Line 151) ack[p] &= arr[p];
    _ARRW(ack, p).__iand__(arr[p])
    # (Line 152) ack[p] -= -2;  // ack[1] = 2
    _ARRW(ack, p).__isub__(-2)
    # (Line 153) const x = ack[p];
    x = ack[p]
    # (Line 154) ack[p] = x & arr[p];  // 2 & 2
    _ARRW(ack, p) << (x & arr[p])
    # (Line 155) arr[p] &= ack[p];
    _ARRW(arr, p).__iand__(ack[p])
    # (Line 156) ret *= ack[p] * arr[p];  // ret = 8
    ret.__imul__(ack[p] * arr[p])
    # (Line 158) arr[p] ^= ack[p];  // arr[1] = 0
    _ARRW(arr, p).__ixor__(ack[p])
    # (Line 159) arr[p] |= ack[0];  // arr[1] = 1
    _ARRW(arr, p).__ior__(ack[0])
    # (Line 160) arr[p] <<= ack[p];  // arr[1] = 4
    _ARRW(arr, p).__ilshift__(ack[p])
    # (Line 161) ret |= arr[p];  // ret = 12
    ret.__ior__(arr[p])
    # (Line 163) if (ack[p] > arr[p]) ret = 0;
    if EUDIf()(_ARRC(ack, p) <= arr[p], neg=True):
        ret << (0)
        # (Line 164) if (arr[p]) ret <<= 1;  // ret = 24
    EUDEndIf()
    if EUDIf()(arr[p]):
        ret.__ilshift__(1)
        # (Line 165) ret -= ack[p] + p / 2;  // ret = 22
    EUDEndIf()
    ret.__isub__(ack[p] + p // 2)
    # (Line 167) switch(arr[p]) {
    EUDSwitch(arr[p])
    # (Line 168) case 4:  // fall-through
    _t3 = EUDSwitchCase()
    # (Line 169) case 1:
    if _t3(4):
        pass
    _t4 = EUDSwitchCase()
    # (Line 170) ret += 1;  // ret = 23
    if _t4(1):
        ret.__iadd__(1)
        # (Line 171) }
    # (Line 172) switch(ack[p]) {
    EUDEndSwitch()
    EUDSwitch(ack[p])
    # (Line 173) case 2:
    _t5 = EUDSwitchCase()
    # (Line 174) break;
    if _t5(2):
        EUDBreak()
        # (Line 175) default:
    # (Line 176) ret = 0;
    if EUDSwitchDefault()():
        ret << (0)
        # (Line 177) }
    # (Line 179) return ret;  // ret = 23
    EUDEndSwitch()
    EUDReturn(ret)
    # (Line 180) }
