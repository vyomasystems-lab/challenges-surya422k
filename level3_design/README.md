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