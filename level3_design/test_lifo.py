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
    