# Full Adder

This example covers the design of a full adder using the functions (sum & carry out) ***S = A ^ B ^ Cin***, and ***Cout = AB + ACin + BCin***. Note that the ^ symbol represents an XOR operation. Moreover, two intermediate signals (P & G) are implemented to simplify the previous functions. These signals are ***P = A ^ B***, and ***G = AB***. As a result, the simplified functions are ***S = P ^ Cin***, and ***Cout = G + Pcin***.

## ystemVerilog:

In this module, there are two internal signals (p & g). Internal signals are declared using the logic type. Moreover, these signals serve as temporary variables (local variables) used to compute a portion of the results. 

```systemverilog
module fulladder(input logic a, b, cin,
                 output logic sum, cout);

    logic p, g;

    assign p = a ^ b;
    assign g = a & b;

    assign sum = p ^ cin;
    assign cout = g | (p & cin);
endmodule
```


## Python:

This fulladder function replicates the behavior of the SV code. However, the functions used to compute the results were implemented directly. Instead of using intermediate signals or local variables, the original functions were used.

```python
def fulladder(a, b, cin):
    psum = a ^ b ^ cin
    pcout = (a & b) |((a^b) & cin)
    return psum, pcout
```


## Python Testbench:

This testbench follows the same procedure explained in the first example. 

```python
import cocotb
from cocotb.triggers import Timer
from model.fulladder_model import fulladder
import random

@cocotb.test()
async def fulladder_random_tb(dut):
    for i in range(20):
        a = random.randint(0, 1)
        b = random.randint(0, 1)
        c = random.randint(0,1)
        dut.a <= a
        dut.b <= b
        dut.cin <= c

        await Timer(2, units='ns')

        cycle = i+1
        psum, pcout = fulladder(a, b, c) #Python adder
        assert dut.sum.value == psum, f"output was incorrect on the {cycle}th cycle:\n" \
                                      f"SV sum is: {dut.sum.value}, " \
                                      f"Python sum is : {psum}"
        assert dut.cout.value == pcout, f"output was incorrect on the {cycle}th cycle:\n" \
                                        f"SV cout is: {dut.cout.value}, " \
                                        f"Python sum is : {pcout}"
```


## Results
![img10](/Images/img10.png)
