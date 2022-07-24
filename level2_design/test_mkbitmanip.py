# See LICENSE.iitm for details
# See LICENSE.vyoma for details

import random
import sys
import cocotb
from cocotb.decorators import coroutine
from cocotb.triggers import Timer, RisingEdge
from cocotb.result import TestFailure
from cocotb.clock import Clock

from model_mkbitmanip import *

# Clock Generation
@cocotb.coroutine
def clock_gen(signal):
    while True:
        signal.value <= 0
        yield Timer(1) 
        signal.value <= 1
        yield Timer(1) 

# Sample Test
@cocotb.test()
def run_test(dut):

    # clock
    cocotb.fork(clock_gen(dut.CLK))

    # reset
    dut.RST_N.value <= 0
    yield Timer(10) 
    dut.RST_N.value <= 1

    ######### CTB : Modify the test to expose the bug #############
    # input transaction
    mav_putvalue_src1 = 0x5
    mav_putvalue_src2 = 0x0
    mav_putvalue_src3 = 0x0
    mav_putvalue_instr = 0x40007033

    # expected output from the model
    expected_mav_putvalue = bitmanip(mav_putvalue_instr, mav_putvalue_src1, mav_putvalue_src2, mav_putvalue_src3)

    # driving the input transaction
    dut.mav_putvalue_src1.value = mav_putvalue_src1
    dut.mav_putvalue_src2.value = mav_putvalue_src2
    dut.mav_putvalue_src3.value = mav_putvalue_src3
    dut.EN_mav_putvalue.value = 1
    dut.mav_putvalue_instr.value = mav_putvalue_instr
  
    yield Timer(1) 

    # obtaining the output
    dut_output = dut.mav_putvalue.value

    cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
    cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')
    
    # comparison
    error_message = f'Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)}'
    assert dut_output == expected_mav_putvalue, error_message

@cocotb.test()
def run_test2(dut):
    cocotb.fork(clock_gen(dut.CLK))

    dut.RST_N.value <= 0;
    yield Timer(10)
    dut.RST_N.value <= 1;

    mav_putvalue_src1 = 0x5
    mav_putvalue_src2 = 0x1
    mav_putvalue_src3 = 0x0
    mav_putvalue_instr = 0x40006033

    expected_mav_putvalue = bitmanip(mav_putvalue_instr,mav_putvalue_src1,mav_putvalue_src2,mav_putvalue_src3)

    dut.mav_putvalue_src1.value = mav_putvalue_src1
    dut.mav_putvalue_src2.value = mav_putvalue_src2
    dut.mav_putvalue_src3.value = mav_putvalue_src3
    dut.EN_mav_putvalue.value = 1
    dut.mav_putvalue_instr.value = mav_putvalue_instr

    yield Timer(1)

    dut_output = dut.mav_putvalue.value

    cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
    cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')

    error_message = f'Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)}'
    assert dut_output == expected_mav_putvalue, error_message

@cocotb.test()
def run_test3(dut):
    cocotb.fork(clock_gen(dut.CLK))

    dut.RST_N.value <= 0;
    yield Timer(10)
    dut.RST_N.value <= 1;

    mav_putvalue_src1 = 0x5
    mav_putvalue_src2 = 0x1
    mav_putvalue_src3 = 0x0
    mav_putvalue_instr = 0x40004033

    expected_mav_putvalue = bitmanip(mav_putvalue_instr,mav_putvalue_src1,mav_putvalue_src2,mav_putvalue_src3)

    dut.mav_putvalue_src1.value = mav_putvalue_src1
    dut.mav_putvalue_src2.value = mav_putvalue_src2
    dut.mav_putvalue_src3.value = mav_putvalue_src3
    dut.EN_mav_putvalue.value = 1
    dut.mav_putvalue_instr.value = mav_putvalue_instr

    yield Timer(1)

    dut_output = dut.mav_putvalue.value

    cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
    cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')

    error_message = f'Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)}'
    assert dut_output == expected_mav_putvalue, error_message

@cocotb.test()
def run_test4(dut):
    cocotb.fork(clock_gen(dut.CLK))

    dut.RST_N.value <= 0;
    yield Timer(10)
    dut.RST_N.value <= 1;

    mav_putvalue_src1 = 0x5
    mav_putvalue_src2 = 0x1
    mav_putvalue_src3 = 0x0
    mav_putvalue_instr = 0x20001033

    expected_mav_putvalue = bitmanip(mav_putvalue_instr,mav_putvalue_src1,mav_putvalue_src2,mav_putvalue_src3)

    dut.mav_putvalue_src1.value = mav_putvalue_src1
    dut.mav_putvalue_src2.value = mav_putvalue_src2
    dut.mav_putvalue_src3.value = mav_putvalue_src3
    dut.EN_mav_putvalue.value = 1
    dut.mav_putvalue_instr.value = mav_putvalue_instr

    yield Timer(1)

    dut_output = dut.mav_putvalue.value

    cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
    cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')

    error_message = f'Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)}'
    assert dut_output == expected_mav_putvalue, error_message

@cocotb.test()
def run_test5(dut):
    cocotb.fork(clock_gen(dut.CLK))

    dut.RST_N.value <= 0;
    yield Timer(10)
    dut.RST_N.value <= 1;

    mav_putvalue_src1 = 0x5
    mav_putvalue_src2 = 0x1
    mav_putvalue_src3 = 0x0
    mav_putvalue_instr = 0x20005033

    expected_mav_putvalue = bitmanip(mav_putvalue_instr,mav_putvalue_src1,mav_putvalue_src2,mav_putvalue_src3)

    dut.mav_putvalue_src1.value = mav_putvalue_src1
    dut.mav_putvalue_src2.value = mav_putvalue_src2
    dut.mav_putvalue_src3.value = mav_putvalue_src3
    dut.EN_mav_putvalue.value = 1
    dut.mav_putvalue_instr.value = mav_putvalue_instr

    yield Timer(1)

    dut_output = dut.mav_putvalue.value

    cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
    cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')

    error_message = f'Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)}'
    assert dut_output == expected_mav_putvalue, error_message

@cocotb.test()
def run_test6(dut):
    cocotb.fork(clock_gen(dut.CLK))

    dut.RST_N.value <= 0;
    yield Timer(10)
    dut.RST_N.value <= 1;

    mav_putvalue_src1 = 0x5
    mav_putvalue_src2 = 0x1
    mav_putvalue_src3 = 0x0
    mav_putvalue_instr = 0x60001033

    expected_mav_putvalue = bitmanip(mav_putvalue_instr,mav_putvalue_src1,mav_putvalue_src2,mav_putvalue_src3)

    dut.mav_putvalue_src1.value = mav_putvalue_src1
    dut.mav_putvalue_src2.value = mav_putvalue_src2
    dut.mav_putvalue_src3.value = mav_putvalue_src3
    dut.EN_mav_putvalue.value = 1
    dut.mav_putvalue_instr.value = mav_putvalue_instr

    yield Timer(1)

    dut_output = dut.mav_putvalue.value

    cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
    cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')

    error_message = f'Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)}'
    assert dut_output == expected_mav_putvalue, error_message

@cocotb.test()
def run_test7(dut):
    cocotb.fork(clock_gen(dut.CLK))

    dut.RST_N.value <= 0;
    yield Timer(10)
    dut.RST_N.value <= 1;

    mav_putvalue_src1 = 0x5
    mav_putvalue_src2 = 0x1
    mav_putvalue_src3 = 0x0
    mav_putvalue_instr = 0x60005033

    expected_mav_putvalue = bitmanip(mav_putvalue_instr,mav_putvalue_src1,mav_putvalue_src2,mav_putvalue_src3)

    dut.mav_putvalue_src1.value = mav_putvalue_src1
    dut.mav_putvalue_src2.value = mav_putvalue_src2
    dut.mav_putvalue_src3.value = mav_putvalue_src3
    dut.EN_mav_putvalue.value = 1
    dut.mav_putvalue_instr.value = mav_putvalue_instr

    yield Timer(1)

    dut_output = dut.mav_putvalue.value

    cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
    cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')

    error_message = f'Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)}'
    assert dut_output == expected_mav_putvalue, error_message

@cocotb.test()
def run_test8(dut):
    cocotb.fork(clock_gen(dut.CLK))

    dut.RST_N.value <= 0;
    yield Timer(10)
    dut.RST_N.value <= 1;

    mav_putvalue_src1 = 0x5
    mav_putvalue_src2 = 0x1
    mav_putvalue_src3 = 0x0
    mav_putvalue_instr = 0x20002033

    expected_mav_putvalue = bitmanip(mav_putvalue_instr,mav_putvalue_src1,mav_putvalue_src2,mav_putvalue_src3)

    dut.mav_putvalue_src1.value = mav_putvalue_src1
    dut.mav_putvalue_src2.value = mav_putvalue_src2
    dut.mav_putvalue_src3.value = mav_putvalue_src3
    dut.EN_mav_putvalue.value = 1
    dut.mav_putvalue_instr.value = mav_putvalue_instr

    yield Timer(1)

    dut_output = dut.mav_putvalue.value

    cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
    cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')

    error_message = f'Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)}'
    assert dut_output == expected_mav_putvalue, error_message

@cocotb.test()
def run_test9(dut):
    cocotb.fork(clock_gen(dut.CLK))

    dut.RST_N.value <= 0;
    yield Timer(10)
    dut.RST_N.value <= 1;

    mav_putvalue_src1 = 0x5
    mav_putvalue_src2 = 0x1
    mav_putvalue_src3 = 0x0
    mav_putvalue_instr = 0x20004033

    expected_mav_putvalue = bitmanip(mav_putvalue_instr,mav_putvalue_src1,mav_putvalue_src2,mav_putvalue_src3)

    dut.mav_putvalue_src1.value = mav_putvalue_src1
    dut.mav_putvalue_src2.value = mav_putvalue_src2
    dut.mav_putvalue_src3.value = mav_putvalue_src3
    dut.EN_mav_putvalue.value = 1
    dut.mav_putvalue_instr.value = mav_putvalue_instr

    yield Timer(1)

    dut_output = dut.mav_putvalue.value

    cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
    cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')

    error_message = f'Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)}'
    assert dut_output == expected_mav_putvalue, error_message

@cocotb.test()
def run_test10(dut):
    cocotb.fork(clock_gen(dut.CLK))

    dut.RST_N.value <= 0;
    yield Timer(10)
    dut.RST_N.value <= 1;

    mav_putvalue_src1 = 0x5
    mav_putvalue_src2 = 0x1
    mav_putvalue_src3 = 0x0
    mav_putvalue_instr = 0x20006033

    expected_mav_putvalue = bitmanip(mav_putvalue_instr,mav_putvalue_src1,mav_putvalue_src2,mav_putvalue_src3)

    dut.mav_putvalue_src1.value = mav_putvalue_src1
    dut.mav_putvalue_src2.value = mav_putvalue_src2
    dut.mav_putvalue_src3.value = mav_putvalue_src3
    dut.EN_mav_putvalue.value = 1
    dut.mav_putvalue_instr.value = mav_putvalue_instr

    yield Timer(1)

    dut_output = dut.mav_putvalue.value

    cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
    cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')

    error_message = f'Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)}'
    assert dut_output == expected_mav_putvalue, error_message

@cocotb.test()
def run_test11(dut):
    cocotb.fork(clock_gen(dut.CLK))

    dut.RST_N.value <= 0;
    yield Timer(10)
    dut.RST_N.value <= 1;

    mav_putvalue_src1 = 0x5
    mav_putvalue_src2 = 0x1
    mav_putvalue_src3 = 0x0
    mav_putvalue_instr = 0x48001033

    expected_mav_putvalue = bitmanip(mav_putvalue_instr,mav_putvalue_src1,mav_putvalue_src2,mav_putvalue_src3)

    dut.mav_putvalue_src1.value = mav_putvalue_src1
    dut.mav_putvalue_src2.value = mav_putvalue_src2
    dut.mav_putvalue_src3.value = mav_putvalue_src3
    dut.EN_mav_putvalue.value = 1
    dut.mav_putvalue_instr.value = mav_putvalue_instr

    yield Timer(1)

    dut_output = dut.mav_putvalue.value

    cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
    cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')

    error_message = f'Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)}'
    assert dut_output == expected_mav_putvalue, error_message

@cocotb.test()
def run_test12(dut):
    cocotb.fork(clock_gen(dut.CLK))

    dut.RST_N.value <= 0;
    yield Timer(10)
    dut.RST_N.value <= 1;

    mav_putvalue_src1 = 0x5
    mav_putvalue_src2 = 0x1
    mav_putvalue_src3 = 0x0
    mav_putvalue_instr = 0x28001033

    expected_mav_putvalue = bitmanip(mav_putvalue_instr,mav_putvalue_src1,mav_putvalue_src2,mav_putvalue_src3)

    dut.mav_putvalue_src1.value = mav_putvalue_src1
    dut.mav_putvalue_src2.value = mav_putvalue_src2
    dut.mav_putvalue_src3.value = mav_putvalue_src3
    dut.EN_mav_putvalue.value = 1
    dut.mav_putvalue_instr.value = mav_putvalue_instr

    yield Timer(1)

    dut_output = dut.mav_putvalue.value

    cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
    cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')

    error_message = f'Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)}'
    assert dut_output == expected_mav_putvalue, error_message

@cocotb.test()
def run_test13(dut):
    cocotb.fork(clock_gen(dut.CLK))

    dut.RST_N.value <= 0;
    yield Timer(10)
    dut.RST_N.value <= 1;

    mav_putvalue_src1 = 0x5
    mav_putvalue_src2 = 0x1
    mav_putvalue_src3 = 0x0
    mav_putvalue_instr = 0x68001033

    expected_mav_putvalue = bitmanip(mav_putvalue_instr,mav_putvalue_src1,mav_putvalue_src2,mav_putvalue_src3)

    dut.mav_putvalue_src1.value = mav_putvalue_src1
    dut.mav_putvalue_src2.value = mav_putvalue_src2
    dut.mav_putvalue_src3.value = mav_putvalue_src3
    dut.EN_mav_putvalue.value = 1
    dut.mav_putvalue_instr.value = mav_putvalue_instr

    yield Timer(1)

    dut_output = dut.mav_putvalue.value

    cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
    cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')

    error_message = f'Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)}'
    assert dut_output == expected_mav_putvalue, error_message

@cocotb.test()
def run_test14(dut):
    cocotb.fork(clock_gen(dut.CLK))

    dut.RST_N.value <= 0;
    yield Timer(10)
    dut.RST_N.value <= 1;

    mav_putvalue_src1 = 0x5
    mav_putvalue_src2 = 0x1
    mav_putvalue_src3 = 0x0
    mav_putvalue_instr = 0x48005033

    expected_mav_putvalue = bitmanip(mav_putvalue_instr,mav_putvalue_src1,mav_putvalue_src2,mav_putvalue_src3)

    dut.mav_putvalue_src1.value = mav_putvalue_src1
    dut.mav_putvalue_src2.value = mav_putvalue_src2
    dut.mav_putvalue_src3.value = mav_putvalue_src3
    dut.EN_mav_putvalue.value = 1
    dut.mav_putvalue_instr.value = mav_putvalue_instr

    yield Timer(1)

    dut_output = dut.mav_putvalue.value

    cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
    cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')

    error_message = f'Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)}'
    assert dut_output == expected_mav_putvalue, error_message

@cocotb.test()
def run_test15(dut):
     cocotb.fork(clock_gen(dut.CLK))
     dut.RST_N.value <= 0
     yield Timer(10)
     dut.RST_N.value <= 1
     mav_putvalue_src1 = 0x5
     mav_putvalue_src2 = 0x1
     mav_putvalue_src3 = 0x0
     mav_putvalue_instr = 0x28005033
     expected_mav_putvalue = bitmanip(mav_putvalue_instr,mav_putvalue_src1,mav_putvalue_src2,mav_putvalue_src3)
     dut.mav_putvalue_src1.value = mav_putvalue_src1
     dut.mav_putvalue_src2.value = mav_putvalue_src2
     dut.mav_putvalue_src3.value = mav_putvalue_src3
     dut.EN_mav_putvalue.value = 1
     dut.mav_putvalue_instr.value = mav_putvalue_instr
     yield Timer(1)
     dut_output = dut.mav_putvalue.value
     cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
     cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')
     error_message = f'Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)}'
     assert dut_output == expected_mav_putvalue, error_message

@cocotb.test()
def run_test16(dut):
     cocotb.fork(clock_gen(dut.CLK))
     dut.RST_N.value <= 0
     yield Timer(10)
     dut.RST_N.value <= 1
     mav_putvalue_src1 = 0x5
     mav_putvalue_src2 = 0x1
     mav_putvalue_src3 = 0x0
     mav_putvalue_instr = 0x68005033
     expected_mav_putvalue = bitmanip(mav_putvalue_instr,mav_putvalue_src1,mav_putvalue_src2,mav_putvalue_src3)
     dut.mav_putvalue_src1.value = mav_putvalue_src1
     dut.mav_putvalue_src2.value = mav_putvalue_src2
     dut.mav_putvalue_src3.value = mav_putvalue_src3
     dut.EN_mav_putvalue.value = 1
     dut.mav_putvalue_instr.value = mav_putvalue_instr
     yield Timer(1)
     dut_output = dut.mav_putvalue.value
     cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
     cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')
     error_message = f'Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)}'
     assert dut_output == expected_mav_putvalue, error_message

@cocotb.test()
def run_test17(dut):
     cocotb.fork(clock_gen(dut.CLK))
     dut.RST_N.value <= 0
     yield Timer(10)
     dut.RST_N.value <= 1
     mav_putvalue_src1 = 0x5
     mav_putvalue_src2 = 0x1
     mav_putvalue_src3 = 0x0
     mav_putvalue_instr = 0x07001033
     expected_mav_putvalue = bitmanip(mav_putvalue_instr,mav_putvalue_src1,mav_putvalue_src2,mav_putvalue_src3)
     dut.mav_putvalue_src1.value = mav_putvalue_src1
     dut.mav_putvalue_src2.value = mav_putvalue_src2
     dut.mav_putvalue_src3.value = mav_putvalue_src3
     dut.EN_mav_putvalue.value = 1
     dut.mav_putvalue_instr.value = mav_putvalue_instr
     yield Timer(1)
     dut_output = dut.mav_putvalue.value
     cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
     cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')
     error_message = f'Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)}'
     assert dut_output == expected_mav_putvalue, error_message

@cocotb.test()
def run_test18(dut):
     cocotb.fork(clock_gen(dut.CLK))
     dut.RST_N.value <= 0
     yield Timer(10)
     dut.RST_N.value <= 1
     mav_putvalue_src1 = 0x5
     mav_putvalue_src2 = 0x1
     mav_putvalue_src3 = 0x0
     mav_putvalue_instr = 0x07005033
     expected_mav_putvalue = bitmanip(mav_putvalue_instr,mav_putvalue_src1,mav_putvalue_src2,mav_putvalue_src3)
     dut.mav_putvalue_src1.value = mav_putvalue_src1
     dut.mav_putvalue_src2.value = mav_putvalue_src2
     dut.mav_putvalue_src3.value = mav_putvalue_src3
     dut.EN_mav_putvalue.value = 1
     dut.mav_putvalue_instr.value = mav_putvalue_instr
     yield Timer(1)
     dut_output = dut.mav_putvalue.value
     cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
     cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')
     error_message = f'Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)}'
     assert dut_output == expected_mav_putvalue, error_message

@cocotb.test()
def run_test19(dut):
     cocotb.fork(clock_gen(dut.CLK))
     dut.RST_N.value <= 0
     yield Timer(10)
     dut.RST_N.value <= 1
     mav_putvalue_src1 = 0x5
     mav_putvalue_src2 = 0x1
     mav_putvalue_src3 = 0x0
     mav_putvalue_instr = 0x04001033
     expected_mav_putvalue = bitmanip(mav_putvalue_instr,mav_putvalue_src1,mav_putvalue_src2,mav_putvalue_src3)
     dut.mav_putvalue_src1.value = mav_putvalue_src1
     dut.mav_putvalue_src2.value = mav_putvalue_src2
     dut.mav_putvalue_src3.value = mav_putvalue_src3
     dut.EN_mav_putvalue.value = 1
     dut.mav_putvalue_instr.value = mav_putvalue_instr
     yield Timer(1)
     dut_output = dut.mav_putvalue.value
     cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
     cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')
     error_message = f'Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)}'
     assert dut_output == expected_mav_putvalue, error_message

@cocotb.test()
def run_test20(dut):
     cocotb.fork(clock_gen(dut.CLK))
     dut.RST_N.value <= 0
     yield Timer(10)
     dut.RST_N.value <= 1
     mav_putvalue_src1 = 0x5
     mav_putvalue_src2 = 0x2
     mav_putvalue_src3 = 0x0
     mav_putvalue_instr = 0x04005033
     expected_mav_putvalue = bitmanip(mav_putvalue_instr,mav_putvalue_src1,mav_putvalue_src2,mav_putvalue_src3)
     dut.mav_putvalue_src1.value = mav_putvalue_src1
     dut.mav_putvalue_src2.value = mav_putvalue_src2
     dut.mav_putvalue_src3.value = mav_putvalue_src3
     dut.EN_mav_putvalue.value = 1
     dut.mav_putvalue_instr.value = mav_putvalue_instr
     yield Timer(1)
     dut_output = dut.mav_putvalue.value
     cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
     cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')
     error_message = f'Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)}'
     assert dut_output == expected_mav_putvalue, error_message