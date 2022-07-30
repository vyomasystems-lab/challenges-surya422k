import random
import sys
import cocotb
from cocotb.decorators import coroutine
from cocotb.triggers import Timer, RisingEdge
from cocotb.result import TestFailure
from cocotb.clock import Clock

@cocotb.coroutine
def clock_gen(signal):
    while(True):
        signal.value <= 0
        yield Timer(1)
        signal.value <= 1 
        yield Timer(1)

@cocotb.test()
def run_test(dut):
    cocotb.fork(clock_gen(dut.clk))

    dut.rstn.value <= 1
    yield Timer(1)
    dut.rstn.value <= 0
    
    dut_in = 0x8
    dut.push.value = 1
    dut.din.value = dut_in

    yield RisingEdge(dut.clk)
    dut.pop.value = 1
    dut_out = dut.dout.Value

    assert dut_out == dut_in


