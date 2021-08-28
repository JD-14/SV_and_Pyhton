# Combinational Logic

This example is a behavioral module that defines the Boolean Function
***y = A’B’C’ + AB’C’ + AB’C***. The module is named "sillyfunction". Moreover,
the module has three inputs, A, B, C, and one oupt, y. Finally, the function
is true when the input is 000, 100, or 101.

## SystemVerilog:
The ***sillyfuction*** module indicates the three inputs ports by using the word ***input***. 
The output port is defined using the word ***output*** and the "logic" (0 or 1) type 
indicates the type of signal. Next, the ***assign*** statement describes combinational logic. 
Moreover, this statement is where the Boolean function is defined, and the output is assigned 
to the output port ***y***. Just as explained in the intro, **~** indicates NOT, **&** 
indicates AND, and **|** indicates OR.

```systemverilog
module sillyfunction(input logic a,b, c,
                     output logic y);

    assign y = ~a & ~b & ~c |
    	        a & ~b & ~c |
    		    a & ~b &  c ;
endmodule
```


## Python:
The sillyfunction function in python only requires the input parameters. The output value
(0 or 1) is returned after the evaluation. The same function was defined using python 
Boolean operators to evaluate the inputs.

```python
def sillyfunction(a, b, c):
    if ( ((not a) & (not b) & (not c)) | (a & (not b) & (not c)) | (a & (not b) & c) ):
        return 1
    else:
        return 0
```


## Python Testbench:
This testbench feeds random inputs (0 or 1) to the device every 2ns. The for-loop repeats the 
input procedure 8 times.  Moreover, the python function is called with the same inputs 
(arguments) as the dut. The last part of the code uses an assert statement to evaluate if the 
output from the python and SV are the same. If the output is not the same, then the test will 
fail and display a predefined message. Important note, cocotb takes in decimal values and converts a decimal to binary and vice versa.

```python
import cocotb
from cocotb.triggers import Timer
from model.sillyfunction_model import sillyfunction
import random

@cocotb.test()
async def silly_random_tb(dut):
    for i in range(8):
        a = random.randint(0, 1)
        b = random.randint(0, 1)
        c = random.randint(0,1)
        dut.a <= a
        dut.b <= b
        dut.c <= c

        await Timer(2, units='ns')

        cycle = i+1
        py = sillyfunction(a, b, c)
        assert dut.y.value == py, f"Randomised test failed on the {cycle}th cycle\n" \
                                  f"Sv y is: {dut.y.value}, " \
                                  f"Python y is: {py}"
```

## Results

![img8](/Images/img8.png)
