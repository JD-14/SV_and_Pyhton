# SystemVerilog & Python

This repository covers seven examples of Hardware Description Language (HDL). The examples covered are based on SystemVerilog (SV) HDL.  Moreover, each example was recreated using python and used to reference the behavior of the SV code. To test a SystemVerilog module, a testbench file written in SystemVerilog is required to run a simulation.  However, the testbenches in this repository were created using a python library named cocotb. Therefore, all the testbenches used for the examples are created using python to make complex tests simpler and easy to create.

# List of Examples:
  1. [Combinational Logic](https://github.com/JD-14/SV_and_Pyhton/tree/main/Code)
  2. [Logic Gates](https://github.com/JD-14/SV_and_Pyhton/tree/main/Code/gates)
  3. [Full Adder](https://github.com/JD-14/SV_and_Pyhton/tree/main/Code/fulladder)
  4. [Register](https://github.com/JD-14/SV_and_Pyhton/tree/main/Code/flop)
  5. Resettable Register:
      1. [Synchronous](https://github.com/JD-14/SV_and_Pyhton/tree/main/Code/flopr/synchronous)
      2. [Asynchronous](https://github.com/JD-14/SV_and_Pyhton/tree/main/Code/flopr/asynchronous)
  7. [Full Adder (Using Nonblocking Assignments)](https://github.com/JD-14/SV_and_Pyhton/tree/main/Code/fulladder2)
  8. [History FSM (Finite State Machine)](https://github.com/JD-14/SV_and_Pyhton/tree/main/Code/historyFSM)


# Brief Intro to SystemVerilog
### 1) Modules:
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

#
### 2) Operator precedence:
Just like in any other programming language, SystemVerilog has arithmetic, shift, and comparison operators. Moreover, the operators have precedence. The image below shows the operators and their precedence.

![img](/Images/img4.png)




# References
  - cocotb:
      - [Documentation](https://docs.cocotb.org/en/stable/index.html)
      - [Github](https://github.com/cocotb/cocotb/tree/ec99a877ee774c33e702391d744fdacb4c87850a)
  - [HDL Intro](http://pages.hmc.edu/harris/cmosvlsi/4e/cmosvlsidesign_4e_App.pdf)
