import random
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

    DIN = 0x8
    dut.din.value = DIN
    dut.push.value = 1
    await FallingEdge(dut.clk)
    dut.push.value = 0
    await FallingEdge(dut.clk)
    DIN2 = 0x10
    dut.din.value = DIN2
    dut.push.value = 1
    await FallingEdge(dut.clk)
    dut.push.value = 0
    dut.pop.value = 1
    await FallingEdge(dut.clk)
    DOUT = dut.dout.value
    dut.pop.value = 0
    
    assert DOUT == DIN2,f"{DOUT} != {DIN2}"



