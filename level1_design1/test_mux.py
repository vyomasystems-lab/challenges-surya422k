# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer
from random import randint

@cocotb.test()
async def mux_test(dut):
    """Test for mux2"""

    INP30 = 1
    SEL = 30

    dut.inp30.value = INP30
    dut.sel.value = SEL
    print("Testing 31X1 MUX")
    await Timer(1,units = 'ns')

    assert dut.out.value == dut.inp30.value, "MUX output is incorrect: {OUT} != {IN}".format(
        OUT = int(dut.out.value), IN = int(dut.inp30.value)
    )

@cocotb.test()   
async def mux_test2(dut):
        INP29 = 1
        SEL = 29

        dut.inp29.value = INP29
        dut.sel.value = SEL

        await Timer(1,units='ns')

        assert dut.out.value == dut.inp29.value, "MUX output is incorrect: {OUT} != {IN}".format(
            OUT = int(dut.out.value), IN = int(dut.inp29.value)
        )
        ##cocotb.log.info('##### CTB: Develop your test here ########')

@cocotb.test()   
async def mux_test3(dut):
        INP = randint(0,3)
        SEL = 5

        dut.inp5.value = INP
        dut.sel.value = SEL

        await Timer(1,units='ns')

        #dut._log.info(f'INP={IN:05} OUT={OUT:05} model={OUT=IN:05} DUT={int(dut.out.value):05}')
        assert dut.out.value == dut.inp5.value, "MUX output is incorrect: {OUT} != {IN}".format(
            OUT = int(dut.out.value), IN = int(dut.inp5.value)
        )
