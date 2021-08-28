# Logic Gates

This example covers a behavioral model that implements combinational logic to create logic gates. The designed gates include AND, OR, XOR NAND, and NOR gates. Moreover, the ports in this example use 2-bit busses.


##SystemVerilog:

The module named gates use the “#(parameter ..)” statement to define the parameter w (width). This parameter represents the value for the width of the busses. In this case, the inputs and outputs have 2-bit busses. To define the width of a bus, the “[#:#]” expression is used in the port declaration. Now to design each gate, the respective logic operators were used, and then each output was assigned to an individual output port. For example, output y1 is the output for the AND gate. Since there are five gates, the outputs are five as well, y1 – y5.

```systemverilog
module gates
       #(parameter w = 2)
       (input logic [w-1:0] a, b,
       output logic [w-1:0] y1, y2, y3, y4, y5);

       /* Five different two-input logic
       * gates acting on #-bit busses*/
       assign y1 = a & b;  //AND
       assign y2 = a | b;  //OR
       assign y3 = a ^ b;  //XOR
       assign y4 = ~(a & b);  //NAND
       assign y5 = ~(a | b);  //NOR
endmodule
```


## Python:

This gate function replicates the behavior of the SV code.

```python
def gates(a, b):
    y1, y2, y3, y4, y5 = 0, 0, 0, 0, 0
    offset = 4
    
    y1 = a & b  #AND
    y2 = a | b  #OR
    y3 = a ^ b  #XOR
    y4 = ~(a & b)+offset #NAND
    y5 = ~(a | b)+offset #NOR

    return y1, y2, y3, y4, y5
```


## Python Testbench:

This testbench follows the same procedure explained in the first example. The only difference is that the input values range from 0 – 3 in decimal. Cocotb takes in decimal values and converts a decimal to binary and vice versa.

```python
import cocotb
from cocotb.triggers import Timer
from model.gates_model import gates
import random

@cocotb.test()
async def gates_random_tb(dut):
    for i in range(20):
        a = random.randint(0, 3)
        b = random.randint(0, 3)
        dut.a <= a
        dut.b <= b

        await Timer(2, units='ns')

        cycle = i+1
        y1, y2, y3, y4, y5 = gates(a, b) #Python Outputs
        assert dut.y1.value == y1, f"Randomised test failed on the {cycle}th cycle\n"\
                                   f"AND gate output is: {dut.y1.value}, "\
                                   f"AND python output is: {y1}"
        assert dut.y2.value == y2, f"Randomised test failed on the {cycle}th cycle\n" \
                                   f"OR gate output is: {dut.y2.value}, " \
                                   f"OR python output is: {y2}"
        assert dut.y3.value == y3, f"Randomised test failed on the {cycle}th cycle\n" \
                                   f"XOR gate output is: {dut.y3.value}, " \
                                   f"XOR python output is: {y3}"
        assert dut.y4.value == y4, f"Randomised test failed on the {cycle}th cycle\n" \
                                   f"NAND gate output is: {dut.y4.value}, " \
                                   f"NAND python output is: {y4}"
        assert dut.y5.value == y5, f"Randomised test failed on the {cycle}th cycle\n" \
                                   f"NOR gate output is: {dut.y5.value}, " \
                                   f"NOR python output is: {y5}"

```


## Results
![img9](/Images/img9.png)
