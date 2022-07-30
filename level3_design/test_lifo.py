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
    await RisingEdge(dut.clk)
    dut.rstn.value = 1
    await RisingEdge(dut.clk)

    DIN = 0x1
    dut.din.value = DIN
    await RisingEdge(dut.clk)
    dut.push.value = 1
    await FallingEdge(dut.clk)

    dut.pop.value = 1
    await RisingEdge(dut.clk)
    DOUT = dut.dout.value
    await RisingEdge(dut.clk)
    
    assert DOUT == DIN,f"{DOUT} != {DIN}"



