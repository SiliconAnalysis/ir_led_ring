import math
import pcbnew

def torad(x):
    return 3.14 * x / 180.

r = 25.
n = 24
theta = 360. / n

i = 0
board = pcbnew.GetBoard()
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


