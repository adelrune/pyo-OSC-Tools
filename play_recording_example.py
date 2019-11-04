from pyo_osc_tools import *
s = Server().boot()
o = OSCRecordSigReader("recording_example")
h1fs = o["hand"][1]["finger"]
s.start()
sls = Pan([
    SineLoop(
        freq=MToF(Scale(h1fs[i]["pos"].sig[0], -400.4, 1144.4, 0, 100)),
        mul=DBToA(Scale(h1fs[i]["pos"].sig[1], 0, 473, -76, -13)),
        feedback=Scale(h1fs[i]["pos"].sig[2], -178, 473, 0, 0.6)
    )
    for i in range(5)
])
o.start()
sls.out()
s.gui(locals)
