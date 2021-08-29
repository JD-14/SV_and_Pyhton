# Register

This example covers the design of a D Flip-Flop. In this design, the positive edge of a clock is used to trigger 
the D Flip-Flop. 

## SystemVerilog:

This module declares an individual input port for the **clock** aside from the rest of the ports. The ports **d** and **q** 
are declared as 2-bit buses. This design incorporates the ***always_ff(…)*** statement to specify the condition that will 
trigger a defined procedure. In this case, the ***posedge clk*** indicates that the defined procedure will execute every time the 
clock's positive edge (rising edge) is fed to the module. The defined procedure copies the value from port **d** to **q**. 
As stated earlier, this only happens on the positive edge of the clock. Note that ***<=*** (nonblocking assignment) is 
used instead of ***=*** (blocking assignment). In SV, nonblocking assignments are used for sequential logic, while 
blocking assignments are used for combinational logic. Moreover, nonblocking assignments are used inside an always 
statement instead of blocking assignments and assign statements

```systemverilog
module flop
       #(parameter w = 2)
       (input logic clk,
       input logic [w-1:0] d,
       output logic [w-1:0] q);

       always_ff @(posedge clk)
        q <= d;
endmodule
```


## Python:

This flop function replicates the behavior of the SV code. Since the python function doesn't require a clock, 
the input value is redirected as the output.

```python
def flop(d):
    return d
```


## Python Testbench:
This testbench uses a predefined function for the ***clock**. The clock is imported from cocotb. Moreover, 
the clock is initialized inside the test function. In this case, the signal is feed to the clock port for a 
period of 10ns. Furthermore, the ***await*** statement uses the ***FallingEgde()*** trigger to wait until the clock 
transition from 1 to 0.

```python
import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer
from model.flop_model import flop
from cocotb.triggers import RisingEdge, FallingEdge, ClockCycles
import random

@cocotb.test()
async def flop_random_tb(dut):
    """ Test that d propagates to q """

    clock = Clock(dut.clk, 10, units="ns")  # Create a 10ns period clock on port clk
    cocotb.fork(clock.start())  # Start the clock

    for i in range(20):
        d = random.randint(0, 3)
        dut.d <= d  # Assign the random value val to the input port d
        
        await FallingEdge(dut.clk)

        cycle = i+1
        pq = flop(d)
        assert dut.q.value == pq,f"output was incorrect on the {cycle}th cycle\n" \
                                 f"SV q is: {dut.q.value}, "\
                                 f"Python q is: {pq} "
```


## Results
![img11](/Images/img11.png)
