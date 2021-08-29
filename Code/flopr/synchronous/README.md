# Synchronous Ressetable Register

This example covers the design of a synchronous register. In this case, the register is a resettable D 
Flip-Flop. In an asynchronous design, the reset only occurs on the rising edge of the clock.

## SystemVerilog:

This module is similar to the module cover in example 4. The difference, in this case, is the implementation 
of the **reset** port. Also, an ***if-else*** statement is implemented as the procedure of the ***always*** 
statement. The procedure assigns the binary value **00** to the output **q** if **reset** is 1 (True). Otherwise, 
the output **q** is the same as the input **d**.

```systemverilog
module flopr
       #(parameter w = 2)
       (input logic clk,
       input logic reset,
       input logic [w-1:0] d,
       output logic [w-1:0] q);

       // Synchronous reset
       always_ff @(posedge clk)
        if (reset) q <= 2'b0;       //using 2 bits
        else q <= d;
endmodule
```


## Python:

This ***flopr*** function replicates the behavior of the SV code. Function only returns the input value 
**d** when **reset** is 0. 

```python
def flopr(d, reset):
    if reset:
        return 0
    else:
        return d
```


## Python Testbench:

This testbench follows the same procedure explained in example 4.

```python
import cocotb
from cocotb.clock import Clock
from model.flopr_model import flopr
from cocotb.triggers import RisingEdge, FallingEdge, ClockCycles
import random

@cocotb.test()
async def flopr_random_tb(dut):
    clock = Clock(dut.clk, 10, units="ns")  # Create a 10ns period clock on port clk
    cocotb.fork(clock.start())  # Start the clock

    for i in range(20):
        d = random.randint(0, 3)
        r = random.randint(0, 1)
        dut.d <= d
        dut.reset <= r

        await FallingEdge(dut.clk)

        cycle = i+1
        pq = flopr(d,r)
        assert dut.q.value == pq, f"output was incorrect on the {cycle}th cycle:\n" \
                                  f"SV q is: {dut.q.value}, " \
                                  f"Python q is: {pq} "
```


## Results
![img](/Images/syn.png)
