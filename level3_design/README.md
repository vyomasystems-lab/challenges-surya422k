# LIFO design Verification

The verification environment is setup using [Vyoma's Uptick Pro](https://vyomasystems.com) provided for the hackathon.

![Screenshot (16)](https://user-images.githubusercontent.com/47589022/182071093-aa1a8f3c-92e2-4b12-870f-4fc6af506d01.png)

## Veirfication Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives input into LIFO module to verify its functionality.

The values are assigned into input ports using
```
\\For push
in = randint(0,255)
dut.din.value = in
dut.push.value = 1

\\For pop
dut.pop.value = 1
out = dut.dout.value
```

Assertion is used to check whether correct output is obtained at correct clock cycle after popping.

```
assert out==in, f"Output Mismatch {out} != {in}"
```

## Test Scenario 1
- Test inputs: in = value between 0 and 255, push = 1, after falling edge, pop = 1
- Expected output: out = value between 0 and 255
- Output observed in DUT: out = 0

Mismatched output indicates a bug in design.

## Design Bug 1
On observing DUT, we can identify that the if statement for the POP operation in LIFO is incorrect
```
else if(pop && empty)
begin
..
end
```
Changing the condition inside if statement as
```
else if(pop && !empty)
```
fixes the bug in the design

## Design Fix 1

Updating design and rerunning makes the test pass. The bug is resolved in lifo_fix.v

![Screenshot (17)](https://user-images.githubusercontent.com/47589022/182159093-2f9af5af-aa20-463f-87bd-10414b0a98f4.png)