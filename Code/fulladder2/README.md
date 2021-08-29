# Full Adder (Using Nonblocking Assignments)

This example is similar to example 3. However, this example demonstrates how using nonblocking assignments leads to an incorrect/problematic model. As explained in example 4, nonblocking assignments are only used for sequential logic. In simple terms in sequential logic means that the present and previous inputs determine the output. This can be an issue if it's not implemented in the correct model. 


## SystemVerilog:

This module substitutes all the ***blocking assignments*** for ***nonblocking assignments***. Note that **nonblocking** assignments can only be implemented inside an ***always*** statement. In this case, the ***always_comb*** (combinational) statement will react to any change in the input ports, **a**, **b**, and **cin**. This **always** statement is the short version for ***always @(a, b, cin)***. Every time an input value changes, this type of **always** statement is used to compute the respective combinational logic (**p**, **g**, **sum**, and **cout**). Moreover, the **nonblocking** assignments are evaluated concurrently. This means that the evaluation/computing of **p**, **g**, **sum**, and **cout** will be at the same time (leaving the new values from **p** and **g** out of the scope for **sum** and **cout**). The issue with using **nonblocking** assignments for combinational logic is the number of times each statement must be evaluated to obtain the correct output. For example, assume the input is 100 (a, b, cin), then after evaluation **p=1**, **p=0**, **sum=0**, and **cout=0**.  The sum is incorrect, but this is because the value of **p** was changed from 0 to 1 during the evaluation. Only during a second evaluation, the **sum** will be computed using the previous value obtained from **p=1**. Moreover, the value of **p** will be updated in **cout** after the second evaluation, and updating the value of **p**, results in **sum=1**, and **cout=0**. This is the reason why using the wrong assignment is a problem. Multiple evaluations result in more time-consuming simulations.


```systemverilog
module fulladder2(input logic a, b, cin,
                 output logic sum, cout);

    logic p, g;

    always_comb
        begin
            p <= a ^ b;  //nonblocking
            g <= a & b;  //nonblocking

            sum <= p ^ cin;
            cout <= g | (p & cin);
        end
endmodule
```


## Python:

This fulladder2 function replicates the behavior of the SV code. This function uses multiple global variables to keep track of previous values. Remember that blocking assignments required previous inputs to determine the output.

```python
a_prev, b_prev, cin_prev = 0, 0, 0
p, g = 0, 0
psum, pcout = 0, 0
delay = 0

def fulladder2(a, b, cin):
    global a_prev, b_prev, cin_prev
    global delay
    global  p, g
    global psum, pcout
    temp_p, temp_g = 0, 0

    temp_p = p
    temp_g = g

    if delay==0:
        delay = 1

        #Store input values
        a_prev = a
        b_prev = b
        cin_prev = cin

        #Compute p & g
        p = a ^ b
        g = a & b
        return p, g, psum, pcout, temp_p, temp_g, 11

    elif (a != a_prev) | (b != b_prev) | (cin != cin_prev):
        #Store input values
        a_prev = a
        b_prev = b
        cin_prev = cin

        #Compute Sum, CarryOut, p, & g
        psum = temp_p ^ cin
        pcout = temp_g | (temp_p & cin)
        p = a ^ b
        g = a & b
        return p, g, psum, pcout, temp_p, temp_g, 22
    else:
        #NO change in inputs, therefore Outputs stays same
        return  temp_p, temp_g, psum, pcout, temp_p, temp_g, 33
```


## Python Testbench:

This testbench follows the same procedure explained in the first example. However, the **binary** file from ***cocotb*** was modified to change the unknown value ***x*** to **0**. This was done to conduct a better comparison of the outputs. Note that at the start of a simulation, some values are initialized to an ***unknown state***, which in this case, after evaluation, results in an ***x*** output.

```python
  
import cocotb
from cocotb.triggers import Timer
from model.fulladder2_model import fulladder2
import random


@cocotb.test()
async def fulladder2_tb(dut):
    for i in range(50):
        a = random.randint(0, 1)
        b = random.randint(0, 1)
        c = random.randint(0,1)
        dut.a <= a
        dut.b <= b
        dut.cin <= c

        await Timer(2, units='ns')

        cycle = i+1
        p, g, psum, pcout, tp, tg, lv = fulladder2(a, b, c)
        assert dut.p.value == p, f"output was incorrect on the {cycle}th cycle\n" \
                                 f"Executed level: {lv}\n" \
                                 f"SV P is: {dut.p.value}, " \
                                 f"Python P is : {p}"
        assert dut.g.value == g, f"output was incorrect on the {cycle}th cycle\n" \
                                 f"Executed level: {lv}\n" \
                                 f"SV P is: {dut.g.value}, " \
                                 f"Python P is : {g}"

        # to solve the 'x' issue change COCOTB_RESOLVE_X to "ZEROS"
        assert dut.sum.value == psum, f"output was incorrect on the {cycle}th cycle\n" \
                                      f"Executed level: {lv}\n" \
                                      f"Prev p, g: {tp}, {tg}\n" \
                                      f"Inputs: {a} {b} {c}\n" \
                                      f"SV sum is: {dut.sum.value} ({dut.p.value}_{dut.g.value}_{dut.sum.value}_{dut.cout.value}), " \
                                      f"Python sum is : {psum} ({p}_{g}_{psum}_{pcout})"
        assert dut.cout.value == pcout, f"output was incorrect on the {cycle}th cycle\n" \
                                        f"Executed level: {lv}\n" \
                                        f"Prev p, g: {tp}, {tg}\n" \
                                        f"Inputs: {a} {b} {c}\n" \
                                        f"SV Cout is: {dut.cout.value} ({dut.p.value}_{dut.g.value}_{dut.sum.value}_{dut.cout.value}), " \
                                        f"Python Cout is : {pcout} ({p}_{g}_{psum}_{pcout})"
```


## Results
![img](/Images/fa2.png)
