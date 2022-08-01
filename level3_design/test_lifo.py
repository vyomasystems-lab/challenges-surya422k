from random import randint
import sys
import cocotb
from cocotb.triggers import Timer, RisingEdge, FallingEdge
from cocotb.clock import Clock

@cocotb.test()
async def run_test(dut):
    clock = Clock(dut.clk,10,units="ns")
    cocotb.start_soon(clock.start())

    dut.rstn.value = 0
    await FallingEdge(dut.clk)
    dut.rstn.value = 1
    await FallingEdge(dut.clk)

    DIN = randint(0,255)
    dut.din.value = DIN
    dut.push.value = 1
    await FallingEdge(dut.clk)
    dut.push.value = 0
    await FallingEdge(dut.clk)
    DIN2 = randint(0,255)
    dut.din.value = DIN2
    dut.push.value = 1
    await FallingEdge(dut.clk)
    dut.push.value = 0
    dut.pop.value = 1
    await FallingEdge(dut.clk)
    dut.pop.value = 0
    await FallingEdge(dut.clk)
    dut.pop.value = 1
    DOUT = dut.dout.value
    await FallingEdge(dut.clk)
    dut.pop.value = 0
    print(f"IN = {DIN2}")
    print(f"OUT = {int(DOUT)}")
    assert DOUT == DIN2,f"{DOUT} != {DIN2}"



