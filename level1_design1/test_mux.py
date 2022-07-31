# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer
from random import randint

@cocotb.test()
async def mux_test(dut):
    """Test for mux2"""

    INP30 = randint(0,3)
    SEL = 30

    dut.inp30.value = INP30
    dut.sel.value = SEL
    print("Testing 31X1 MUX")
    await Timer(1,units = 'ns')

    assert dut.out.value == dut.inp30.value, "MUX output is incorrect: {OUT} != {IN}".format(
        OUT = int(dut.out.value), IN = int(dut.inp30.value)
    )