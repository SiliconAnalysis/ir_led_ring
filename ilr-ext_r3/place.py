import math
import pcbnew

def torad(x):
    return 3.14 * x / 180.

def leds():
    r = 25.
    n = 24
    theta = 360. / n

    i = 0
    for m in list(board.m_Modules):
        print
        print m.GetReference()
        if m.GetReference()[0] != 'D':
            continue
        if m.GetReference() == 'D1':
            continue

        print i
        a = i * theta
        # center at pin 1 (left)
        # but component is flipped for power orientation
        #x = r * math.sin(torad(a)) + 1.27
        # or not? w/e
        x = r * math.sin(torad(a))
        y = r * math.cos(torad(a))

        xnew = x + 100
        ynew = 100 - y
        # in 10ths of degree
        anew = 10 * (360 - (a + 180))
        print 'x = %0.1f' % (xnew)
        print 'y = %0.1f' % (ynew)
        print 'a = %u' % anew

        # in nm...we have mm
        m.SetPosition(pcbnew.wxPoint(xnew * 1e6, ynew * 1e6))
        m.SetOrientation(anew)

        i += 1

def get_module(designator):
    for m in list(board.m_Modules):
        if m.GetReference() == designator:
            return m
    raise ValueError(designator)

def boardxy(x):
    return x * 25.4 * 1e6

def mounting():
    cx = 3.937007874
    cy = 3.937007874
    d = 5.118110236 - 3.937007874
    n = 3

    def rad(d):
        return math.pi * d / 180.

    for i in xrange(n):
        print
        print i
        j = 'J%u' % (i + 2,)
        m = get_module(j)
        angle = rad(360 / n * i - 5)
        dx = d * math.sin(angle)
        dy = d * math.cos(angle)
        print dx, dy
        x = cx + dx
        y = cy + dy
        print 'X %0.3f' % x
        print 'Y %0.3f' % y
        m.SetPosition(pcbnew.wxPoint(boardxy(x), boardxy(y)))

board = pcbnew.GetBoard()
leds()
mounting()

