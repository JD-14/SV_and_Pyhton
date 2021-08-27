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
  - Modules:
    - a.	A block of hardware with inputs and outputs is called a module. A module always begins with the word “module”, followed by the given name of the module and its list of the inputs and outputs. Moreover, the list of inputs and outputs are also known as ports. The middle of the module contains the description of a desired functionality. There are two styles for describing a module functionality. These styles are behavioral and structural. Finally, a module is always ended with the statement “endmodule”. 


# References
  - cocotb:
      - [Documentation](https://docs.cocotb.org/en/stable/index.html)
      - [Github](https://github.com/cocotb/cocotb/tree/ec99a877ee774c33e702391d744fdacb4c87850a)
      - [HDL](http://pages.hmc.edu/harris/cmosvlsi/4e/cmosvlsidesign_4e_App.pdf)
