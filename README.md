# SystemVerilog & Python

This repository covers seven examples of Hardware Description Language (HDL). The examples covered are based on SystemVerilog (SV) HDL.  Moreover, each example was recreated using python and used to reference the behavior of the SV code. To test a SystemVerilog module, a testbench file written in SystemVerilog is required to run a simulation.  However, the testbenches in this repository were created using a python library named cocotb. Therefore, all the testbenches used for the examples are created using python to make complex tests simpler and easy to create.

# List of Examples:
  1. [Combinational Logic](/Code/sillyfunction/)
  2. [Logic Gates](https://github.com/JD-14/SV_and_Pyhton/tree/main/Code/gates)
  3. [Full Adder](https://github.com/JD-14/SV_and_Pyhton/tree/main/Code/fulladder)
  4. [Register](https://github.com/JD-14/SV_and_Pyhton/tree/main/Code/flop)
  5. Resettable Register:
      1. [Synchronous](https://github.com/JD-14/SV_and_Pyhton/tree/main/Code/flopr/synchronous)
      2. [Asynchronous](https://github.com/JD-14/SV_and_Pyhton/tree/main/Code/flopr/asynchronous)
  7. [Full Adder (Using Nonblocking Assignments)](https://github.com/JD-14/SV_and_Pyhton/tree/main/Code/fulladder2)
  8. [History FSM (Finite State Machine)](https://github.com/JD-14/SV_and_Pyhton/tree/main/Code/historyFSM)


# Brief Intro to SystemVerilog
## 1) Modules:
A block of hardware with inputs and outputs is called a module. A module always begins with the word “module”, followed by the given name of the module and its list of the inputs and outputs. Moreover, the list of inputs and outputs are also known as ports. The middle of the module contains the description of a desired functionality. There are two styles for describing a module functionality. These styles are behavioral and structural. Finally, a module is always ended with the statement “endmodule”.
    
> The image below is an example of a module. The module's name is “sillyfunction” and the ports are a, b, c, and y. Moreover, notice how the “input” statement defines ports a, b, and c as inputs., the “output” statement defines port y as output, and "wire" is used to read the output value. Next, the “assign” statement describes the module functionality. This functionality will be cover in detail later in the report. Finally, the module ends with the statement “endmodeule”.
>
> ![img](/Images/img1.png)

   1. Behavioral Modules:
      > Behavioral models describe what a module does. In simple terms, the module's functionality is fully described in the same module using the desired operators, numbers, and statements. The image below is an example of behavioral modeling. This module uses an “assign” statement to describe a 3-input AND gate using the logic AND (&) operators.
      >
      > ![img](/Images/img2.png)


   2. Structural modules:
      > Structural models describe how a module is built from simpler modules. In simple terms, a module calls a different module to describe its functionality. It is important to know that the module that is called must be defined elsewhere in the code.  The image below is an example of structural modeling. The image shows that the “ANDgate” module uses the “AND3” module to describe its functionality. Moreover, the “AND3” inside the “ANDgate” is called an instance (copy). An instance is given an arbitrary name after the name of the module that it's been called. In this case the instance is named “results”. 
      >
      > ![img](/Images/img3.png)

## 2) Operator precedence:
Just like in any other programming language, SystemVerilog has arithmetic, shift, and comparison operators. Moreover, the operators have precedence. The image below shows the operators and their precedence.

![img](/Images/img4.png)


## 3) Numbers:
In SystemVerilog, there is a simple way to define number values. This method is useful when working with large-bit buses. The format for declaring a number value is “N’Bvalue”, where N is the size in bits, B is the base, and “value” gives the value. For example, “3’b101” indicates a 3-bit number with a binary value of 101. There are multiple base options to declare a value, ‘b for binary (base 2), ‘o for octal (base 8), ‘d for decimal (base 10), and ‘h for hexadecimal (base 16).  Moreover, the defaults base is decimal. Furthermore, if a declared value doesn’t match the bit size (or size is omitted), zeros are automatically padded on the front of the value. For example, “ ’b11” gives the value 0000…011.  Finally, A useful shortcut to fill the value with all 0s or 1s is to use the declaration ‘0 or ‘1, respectively. The image below shows more examples of number declarations.

![img](/Images/img5.png)


## 4) Zs and Xs (signal values):
SystemVerilog uses “z” to indicate a floating value (represents an open circuit). The “x” value is used to indicate an invalid logic level (bug or error). Moreover, a gate that receives a floating input (z) may produce an x output when it can’t determine the correct output value. The image below shows the truth table of an AND gate with all possible combinations of z and x.

![img](/Images/img6.png)


## 5) Testbench
A testbench is a module used to test another module. The tested module is called the Device Under Test (DUT). Using a series of desired input patterns called test vectors are used to generate an output. Then the outputs/results are inspected to verify if the correct outputs were produced.  

>The image below shows a sample testbench for the “ANDgate” module. The first line indicates the value of each time unit (timescale). The format is “ ‘time-scale unit / step ”. In this case, each unit is 1ns, and the simulation has 1ns resolution. The second line marks the beginning of the module. The third and fourth lines define the input (reg) and output (wire) ports. The sixth and seventh line mark the beginning of the simulation. The seventh line creates files that stores the results from the simulation. The eighth line creates a file with all the variables use during the simulation. Lines 9-24 show the 8 possible input patterns use during the simulation. Moreover the “#” symbol is used to indicate a delay of 10ns between each pattern. Line 27 indicates that after the 10ns the simulation stops. Line 27 terminates the simulation. Line 28 marks the end of the simulation. Line 30 is the device under test (ANDgate). Finally, line 31 marks the end of the module.
> 
> ![img](/Images/img7.png)


# Testbench with cocotb

The cocotb library allows you to create testbenches using python instead of SystemVerilog (SV). The python code below is the equivalent of the SystemVerilog testbench presented earlier.  The first line imports the cocotb library.  The second line imports the timer that is used to delay the input signals. This is the equivalent of the “#” in SV. The third line imports the hardware design of the 3-input AND gate.  Line five shows the decorator from cocotb used to indicate the beginning of the simulation.  Line six defines the beginning of the test to be implemented. This is equivalent to the “ANDgate_testbench” module (line 2) in SV.  Moreover, line six uses the argument “dut” to indicate the “ANDgate” module is the Device Under Test (dut).  Line seven, defines the input variables and its valuesLine eight, shows the input values to be feed to the device (AND gate). The “dut.a” indicates the port “a” of the device, and “<=” serves as the assignment operator that indicates the where the input value is to be feed. Line nine, sets a timer that indicates how long the input signals will last. this case the inputs values last for 10ns.  From this point the same techniques are applied to the rest of the inputs.

```python
import cocotb
from cocotb.triggers import Timer
from model.gates_model import ANDgate

@cocotb.test()
async def ANDgate_testbench(dut):
    a, b, c = 0, 0, 0
    dut.a <= a, dut.b <= b, dut.c <= c
    await Timer(10, units='ns')

    a, b, c = 0, 0, 1
    dut.a <= a, dut.b <= b, dut.c <= c
    await Timer(10, units='ns')

    a, b, c = 0, 1, 0
    dut.a <= a, dut.b <= b, dut.c <= c
    await Timer(10, units='ns')

    a, b, c = 0, 1, 1
    dut.a <= a, dut.b <= b, dut.c <= c
    await Timer(10, units='ns')

    a, b, c = 1, 0, 0
    dut.a <= a, dut.b <= b, dut.c <= c
    await Timer(10, units='ns')

    a, b, c = 1, 0, 1
    dut.a <= a, dut.b <= b, dut.c <= c
    await Timer(10, units='ns')

    a, b, c = 1, 1, 0
    dut.a <= a, dut.b <= b, dut.c <= c
    await Timer(10, units='ns')

    a, b, c = 1, 1, 1
    dut.a <= a; dut.b <= b, dut.c <= c
    await Timer(10, units='ns')
```




# References
  - cocotb:
      - [Documentation](https://docs.cocotb.org/en/stable/index.html)
      - [Github](https://github.com/cocotb/cocotb/tree/ec99a877ee774c33e702391d744fdacb4c87850a)
  - [HDL Intro](http://pages.hmc.edu/harris/cmosvlsi/4e/cmosvlsidesign_4e_App.pdf)
