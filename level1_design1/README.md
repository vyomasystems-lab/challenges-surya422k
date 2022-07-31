# 31-to-1 MUX Design Verification

The verification environment is setup using [Vyoma's Uptick Pro](https://vyomasystems.com) provided for the hackathon.
<<<<<<< HEAD
=======

![Screenshot (12)](https://user-images.githubusercontent.com/47589022/182037448-29546b61-cf83-4c9a-be21-8dd3ec8ea6f7.png)


>>>>>>> c5cddb1303b83ca70002822a273a579bf710b01e

##Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives input into 31-to-1 MUX (Design Under Test) and verifies the correctiveness of the output.

The values are assigned into input ports using 
```
For port 30 of MUX
inp = randint(0,3)
dut.inp30.value = inp
dut.sel.value = 30
```