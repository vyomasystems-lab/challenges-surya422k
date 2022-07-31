# 31-to-1 MUX Design Verification

The verification environment is setup using [Vyoma's Uptick Pro](https://vyomasystems.com) provided for the hackathon.

![Screenshot (12)](https://user-images.githubusercontent.com/47589022/182037448-29546b61-cf83-4c9a-be21-8dd3ec8ea6f7.png)

## Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives input into 31-to-1 MUX (Design Under Test) and verifies the correctiveness of the output.

The values are assigned into input ports using 
```
For port 30 of MUX
inp = randint(0,3)
dut.inp30.value = inp
dut.sel.value = 30
```
Assert statement is used for comparing the output of the DUT with the expected output according to the operation.

```
assert dut.out.value == dut.inp30.value, "MUX output is incorrect: {OUT} != {IN}".format(
        OUT = int(dut.out.value), IN = int(dut.inp30.value)
    )
```

## Test Scenario 1
- Test inputs: sel = 30, inp30 = 8
- Expected Output: out = 8
- Observed output in the DUT: out = 0

Mismatched output indicates a bug is present in the DUT. 

## Design Bug 1
On observing the DUT, we can find that the case statement for value 30 of 5-bit sel value is missing
```
    5'b11101: out = inp29;
    default: out = 0;
```
We need to add another case for 31 as
```
    5'b11110: out = inp30;
```
## Design Fix 1

Updating design and rerunning makes the test pass. The bug is resolves in mux_fix.v

![Screenshot (13)](https://user-images.githubusercontent.com/47589022/182038345-6db9c23c-1c6a-4552-beb2-ab065e75c6d3.png)

## Test scenario 2
- Test inputs: inp12 = 16, sel = 12
- Expected Output: out = 12
- Observed output at DUT: out = 0

## Design bug 2

Inside the switch-case statement for sel input, inp12 is assigned for sel value 13, so the result becomes 0

```
    5'b01101: out = inp12;
    5'b01101: out = inp13;
```
We need to change the address value in inp12 to 5'b01100

## Design Fix

