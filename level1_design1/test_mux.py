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

@cocotb.test()
async def mux_test1(dut):
    inp = randint(0,3)
    SEL = 1
    dut.inp1.value = inp
    dut.sel.value = SEL
    await Timer(1,units="us")
    assert dut.out.value == dut.inp1.value, "MUX output is incorrect"

@cocotb.test()
async def mux_test2(dut):
    inp = randint(0,3)
    SEL = 2
    dut.inp2.value = inp
    dut.sel.value = SEL
    await Timer(1,units="us")
    assert dut.out.value == dut.inp2.value, "MUX output is incorrect"

@cocotb.test()
async def mux_test3(dut):
    inp = randint(0,3)
    SEL = 3
    dut.inp3.value = inp
    dut.sel.value = SEL
    await Timer(1,units="us")
    assert dut.out.value == dut.inp3.value, "MUX output is incorrect"

@cocotb.test()
async def mux_test4(dut):
    inp = randint(0,3)
    SEL = 4
    dut.inp4.value = inp
    dut.sel.value = SEL
    await Timer(1,units="us")
    assert dut.out.value == dut.inp4.value, "MUX output is incorrect"

@cocotb.test()
async def mux_test5(dut):
    inp = randint(0,3)
    SEL = 5
    dut.inp5.value = inp
    dut.sel.value = SEL
    await Timer(1,units="us")
    assert dut.out.value == dut.inp5.value, "MUX output is incorrect"

@cocotb.test()
async def mux_test6(dut):
    inp = randint(0,3)
    SEL = 6
    dut.inp6.value = inp
    dut.sel.value = SEL
    await Timer(1,units="us")
    assert dut.out.value == dut.inp6.value, "MUX output is incorrect"

@cocotb.test()
async def mux_test7(dut):
    inp = randint(0,3)
    SEL = 7
    dut.inp7.value = inp
    dut.sel.value = SEL
    await Timer(1,units="us")
    assert dut.out.value == dut.inp7.value, "MUX output is incorrect"
    
@cocotb.test()
async def mux_test8(dut):
    inp = randint(0,3)
    SEL = 8
    dut.inp8.value = inp
    dut.sel.value = SEL
    await Timer(1,units="us")
    assert dut.out.value == dut.inp8.value, "MUX output is incorrect"

@cocotb.test()
async def mux_test9(dut):
    inp = randint(0,3)
    SEL = 9
    dut.inp9.value = inp
    dut.sel.value = SEL
    await Timer(1,units="us")
    assert dut.out.value == dut.inp9.value, "MUX output is incorrect"

@cocotb.test()
async def mux_test10(dut):
    inp = randint(0,3)
    SEL = 10
    dut.inp10.value = inp
    dut.sel.value = SEL
    await Timer(1,units="us")
    assert dut.out.value == dut.inp10.value, "MUX output is incorrect"

@cocotb.test()
async def mux_test11(dut):
    inp = randint(0,3)
    SEL = 11
    dut.inp11.value = inp
    dut.sel.value = SEL
    await Timer(1,units="us")
    assert dut.out.value == dut.inp11.value, "MUX output is incorrect"

@cocotb.test()
async def mux_test12(dut):
    inp = randint(0,3)
    SEL = 12
    dut.inp12.value = inp
    dut.sel.value = SEL
    await Timer(1,units="us")
    assert dut.out.value == dut.inp12.value, "MUX output is incorrect"

@cocotb.test()
async def mux_test13(dut):
    inp = randint(0,3)
    SEL = 13
    dut.inp13.value = inp
    dut.sel.value = SEL
    await Timer(1,units="us")
    assert dut.out.value == dut.inp13.value, "MUX output is incorrect"

@cocotb.test()
async def mux_test14(dut):
    inp = randint(0,3)
    SEL = 14
    dut.inp14.value = inp
    dut.sel.value = SEL
    await Timer(1,units="us")
    assert dut.out.value == dut.inp14.value, "MUX output is incorrect"

@cocotb.test()
async def mux_test15(dut):
    inp = randint(0,3)
    SEL = 15
    dut.inp15.value = inp
    dut.sel.value = SEL
    await Timer(1,units="us")
    assert dut.out.value == dut.inp15.value, "MUX output is incorrect"

@cocotb.test()
async def mux_test16(dut):
    inp = randint(0,3)
    SEL = 16
    dut.inp16.value = inp
    dut.sel.value = SEL
    await Timer(1,units="us")
    assert dut.out.value == dut.inp16.value, "MUX output is incorrect"

@cocotb.test()
async def mux_test17(dut):
    inp = randint(0,3)
    SEL = 17
    dut.inp17.value = inp
    dut.sel.value = SEL
    await Timer(1,units="us")
    assert dut.out.value == dut.inp17.value, "MUX output is incorrect"

@cocotb.test()
async def mux_test18(dut):
    inp = randint(0,3)
    SEL = 18
    dut.inp18.value = inp
    dut.sel.value = SEL
    await Timer(1,units="us")
    assert dut.out.value == dut.inp18.value, "MUX output is incorrect"

@cocotb.test()
async def mux_test19(dut):
    inp = randint(0,3)
    SEL = 19
    dut.inp19.value = inp
    dut.sel.value = SEL
    await Timer(1,units="us")
    assert dut.out.value == dut.inp19.value, "MUX output is incorrect"

@cocotb.test()
async def mux_test20(dut):
    inp = randint(0,3)
    SEL = 20
    dut.inp20.value = inp
    dut.sel.value = SEL
    await Timer(1,units="us")
    assert dut.out.value == dut.inp20.value, "MUX output is incorrect"

@cocotb.test()
async def mux_test21(dut):
    inp = randint(0,3)
    SEL = 21
    dut.inp21.value = inp
    dut.sel.value = SEL
    await Timer(1,units="us")
    assert dut.out.value == dut.inp21.value, "MUX output is incorrect"

@cocotb.test()
async def mux_test22(dut):
    inp = randint(0,3)
    SEL = 22
    dut.inp22.value = inp
    dut.sel.value = SEL
    await Timer(1,units="us")
    assert dut.out.value == dut.inp22.value, "MUX output is incorrect"

@cocotb.test()
async def mux_test23(dut):
    inp = randint(0,3)
    SEL = 23
    dut.inp23.value = inp
    dut.sel.value = SEL
    await Timer(1,units="us")
    assert dut.out.value == dut.inp23.value, "MUX output is incorrect"

@cocotb.test()
async def mux_test24(dut):
    inp = randint(0,3)
    SEL = 24
    dut.inp24.value = inp
    dut.sel.value = SEL
    await Timer(1,units="us")
    assert dut.out.value == dut.inp24.value, "MUX output is incorrect"

@cocotb.test()
async def mux_test25(dut):
    inp = randint(0,3)
    SEL = 25
    dut.inp25.value = inp
    dut.sel.value = SEL
    await Timer(1,units="us")
    assert dut.out.value == dut.inp25.value, "MUX output is incorrect"

@cocotb.test()
async def mux_test26(dut):
    inp = randint(0,3)
    SEL = 26
    dut.inp26.value = inp
    dut.sel.value = SEL
    await Timer(1,units="us")
    assert dut.out.value == dut.inp26.value, "MUX output is incorrect"

@cocotb.test()
async def mux_test27(dut):
    inp = randint(0,3)
    SEL = 27
    dut.inp27.value = inp
    dut.sel.value = SEL
    await Timer(1,units="us")
    assert dut.out.value == dut.inp27.value, "MUX output is incorrect"

@cocotb.test()
async def mux_test28(dut):
    inp = randint(0,3)
    SEL = 28
    dut.inp28.value = inp
    dut.sel.value = SEL
    await Timer(1,units="us")
    assert dut.out.value == dut.inp28.value, "MUX output is incorrect"

@cocotb.test()
async def mux_test29(dut):
    inp = randint(0,3)
    SEL = 29
    dut.inp29.value = inp
    dut.sel.value = SEL
    await Timer(1,units="us")
    assert dut.out.value == dut.inp29.value, "MUX output is incorrect"

@cocotb.test()
async def mux_test30(dut):
    inp = randint(0,3)
    SEL = 30
    dut.inp30.value = inp
    dut.sel.value = SEL
    await Timer(1,units="us")
    assert dut.out.value == dut.inp30.value, "MUX output is incorrect"