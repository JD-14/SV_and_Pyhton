# a

This example is the **asynchronous** version of example 5.1, which was cover previously. An asynchronous reset occurs 
immediately. This means that the register will immediately respond to the rising edge on **reset**.

## SystemVerilog:

This module is similar to the module covered in example 5.1. However, in this example, the ***always*** statement 
includes the **reset** port. This means that the statement will react to the positive edge of the **reset**. 

```systemverilog
module flopr2
       #(parameter w = 2)
       (input logic clk,
       input logic reset,
       input logic [w-1:0] d,
       output logic [w-1:0] q);

       // Asynchronous reset
       always_ff @(posedge clk, posedge reset)
        if (reset) q <= 2'b0;       //using 2 bits
        else q <= d;
endmodule
```


## Python:

This flopr2 function replicates the behavior of the SV code.  

```python
def flopr2(d, reset):
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
from model.flopr2_model import flopr2
from cocotb.triggers import RisingEdge, FallingEdge, ClockCycles, Edge
import random

@cocotb.test()
async def flopr2_random_tb(dut):
    clock = Clock(dut.clk, 10, units="ns")  # Create a 10ns period clock on port clk
    cocotb.fork(clock.start())  # Start the clock

    for i in range(20):
        d = random.randint(0, 3)
        r = random.randint(0, 1)
        dut.d <= d
        dut.reset <= r

        await FallingEdge(dut.clk)

        cycle = i+1
        pq = flopr2(d, r)
        assert dut.q.value == pq, f"output was incorrect on the {cycle}th cycle:\n" \
                                  f"SV q is: {dut.q.value}, " \
                                  f"Python q is: {pq} "
```


## Results
![img](/Images/asyn.png)
