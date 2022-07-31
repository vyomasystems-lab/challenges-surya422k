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
## Design Fix
