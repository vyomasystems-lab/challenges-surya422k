# BitManip Co-Processor Verification

The verification environment is setup using [Vyoma's Uptick Pro](https://vyomasystems.com) provided for the hackathon.

![Screenshot (15)](https://user-images.githubusercontent.com/47589022/182070760-7e79ab7b-54fa-470d-b7aa-d1af2c34de40.png)

## Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives the source values and instruction to the coprocessor to verify its functionality.

The values are assigned to the input ports using 
```
//For ANDN operation
mav_putvalue_src1 = 0x1
mav_putvalue_src1 = 0x1
mav_putvalue_src1 = 0x0
mav_putvalue_instr = 0x40007033
dut.mav_putvalue_src1.value = mav_putvalue_src1
dut.mav_putvalue_src2.value = mav_putvalue_src2
dut.mav_putvalue_src3.value = mav_putvalue_src3
dut.EN_mav_putvalue.value = 1
dut.mav_putvalue_instr.value = mav_putvalue_instr
```
Assertion is used for checking the bugs in the DUT

```
error_message = f'Value mismatch DUT = {hex(dut_output)   does not match MODEL = {hex(expected_mav_putvalue)}' 
assert dut_output == expected_mav_putvalue, error_message
```

## Test Scenario 1
- Test inputs: mav_putvalue_src1 = 0x1, mav_putvalue_src1 = 0x1, mav_putvalue_src1 = 0x1, mav_putvalue_instr = 0x40007033
- Expected Output: mav_putvalue = 0x11
- Output from DUT: mav_putvalue = 0x1

The outputs are mismatched since there is a bug in the design.
