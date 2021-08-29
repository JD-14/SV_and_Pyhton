# History FSM (Finite State Machine)

This example covers the design for a ***finite state machine***. To be more specific, the design implemented is a ***Mealy machine***. This means that the output is a function of the current state and inputs. The image below shows the transition diagram of the Mealy machine implemented in this example. This machine has an input **a** and two outputs, **x** and **y**.  Output **x** is true when the input is the same now as it was in the last cycle. Output **y** is true when the input is the same now as it was for the past two cycles. If the machine is **reset**, the cycle will start from **0**.

![img](/Images/his_dia.png)

## SystemVerilog:

In this module, the ***typedef*** statement defines ***statetype*** as a 3-bit logic value with one of four possibilities: **S0**, **S1**, **S2**, **S3**, or **S4**. The ***enum*** (enumerate) encodings default to numerical order: **S0=000**, **S1=001**, **S2=010**, **S3=011**, or **S4=100**. Next, the **state** and **nextstate** are declared as **statetype** signals.  To get the **nextstate** of the current state, a ***case*** statement is used to define the state transition table.

```systemverilog
module historyFSM(input logic clk,
                  input logic reset,
                  input logic a,
                  output logic x, y);

                  typedef enum logic [2:0]
                    {S0, S1, S2, S3, S4} statetype;
                  statetype state, nextstate;

                  // State Register
                  always_ff @(posedge clk)
                    if (reset) state <= S0;
                    else       state <= nextstate;

                  // Next State Logic
                  always_comb
                    case (state)
                        S0: if (a) nextstate = S3;
                            else   nextstate = S1;
                        S1: if (a) nextstate = S3;
                            else   nextstate = S2;
                        S2: if (a) nextstate = S3;
                            else   nextstate = S2;
                        S3: if (a) nextstate = S4;
                            else   nextstate = S1;
                        S4: if (a) nextstate = S4;
                            else   nextstate = S1;
                        default:   nextstate = S0;
                    endcase

    // Output Logic
    assign x = ((state == S1 | state == S2) & ~a) |
               ((state == S3 | state == S4) & a);
    assign y = (state == S2 & ~a) | (state == S4 & a);
endmodule

```

## Python:

This ***historyFSM*** function replicates the behavior of the SV code. This function uses multiple global variables to keep track of previous values.

```python
state, nextstate = 0, 0
num_calls = 0
start = 1
a_prev = 0
def historyFSM(rst, a,):
    global state, nextstate
    global start
    global num_calls
    global a_prev

    #Store the previous values of state & nextstate
    temp_s, temp_n = state, nextstate

    if start:
        start = 0
        if rst:
            state = 0
        else:
            state = nextstate

        if state == 0:
            nextstate = 3 if a else 1
        elif state == 1:
            nextstate = 3 if a else 2
        elif state == 2:
            nextstate = 3 if a else 2
        elif state == 3:
            nextstate = 4 if a else 1
        elif state == 4:
            nextstate = 4 if a else 1
        else:
            nextstate = 0
    else:
        if rst:
            state = 0
        else:
            state = nextstate

        if (rst==0) & (a != a_prev):
            for i in range(2):
                state = nextstate

                if state == 0:
                    nextstate = 3 if a else 1
                elif state == 1:
                    nextstate = 3 if a else 2
                elif state == 2:
                    nextstate = 3 if a else 2
                elif state == 3:
                    nextstate = 4 if a else 1
                elif state == 4:
                    nextstate = 4 if a else 1
                else:
                    nextstate = 0
        else:
            if state == 0:
                nextstate = 3 if a else 1
            elif state == 1:
                nextstate = 3 if a else 2
            elif state == 2:
                nextstate = 3 if a else 2
            elif state == 3:
                nextstate = 4 if a else 1
            elif state == 4:
                nextstate = 4 if a else 1
            else:
                nextstate = 0

    num_calls += 1
    a_prev = a
    x = (((state == 1) | (state == 2)) & (not a)) | (((state == 3) | (state == 4)) & a)
    y = ((state == 2) & (not a)) | ((state == 4) & a)
    return int(x), int(y), state, nextstate, temp_s, temp_n, num_calls
```


## Python Testbench:

This testbench follows the same procedure explained in the first example. However, a ***print*** function was implemented to track all the inputs and their respective outputs.

```python
import cocotb
from cocotb.clock import Clock
from model.historyFSM_model import historyFSM
from cocotb.triggers import RisingEdge, FallingEdge, ClockCycles
import random

@cocotb.test()
async def historyFSM_random_tb(dut):
    clock = Clock(dut.clk, 10, units="ns")  # Create a 10ns period clock on port clk
    cocotb.fork(clock.start())  # Start the clock

    for i in range(20):
        a = random.randint(0, 1)
        r = random.randint(0, 1)
        dut.a <= a
        dut.reset <= r

        await FallingEdge(dut.clk)

        cycle = i+1
        px, py, pstate, pnext, ps, pn, n_c= historyFSM(r, a)  #Python model
        print(f"{cycle} cycle inputs (r, a): {r}, {a} -----> (sv state, next: { dut.state.value} {dut.nextstate.value})"\
              f"  (python state, next: {pstate}, {pnext})\n")

        assert dut.state.value == pstate, f"Output was incorrect on the {cycle}th (p={n_c}) cycle\n" \
                                          f"Inputs: {r}, {a}\n" \
                                          f"SV state is: {dut.state.value}" \
                                          f"Python state is: {pstate} (prev: state, next = {ps} {pn})"
        assert dut.nextstate.value == pnext, f"Output was incorrect on the {cycle}th (p={n_c}) cycle\n" \
                                             f"Inputs: {r}, {a}\n" \
                                             f"SV next is: {dut.nextstate.value}, " \
                                             f"Python next is: {pnext} (prev: state, next = {ps} {pn})"
        assert dut.x.value == px, f"Output was incorrect on the {cycle}th (p={n_c})  cycle\n" \
                                  f"Inputs: {r}, {a}\n" \
                                  f"SV x is: {dut.x.value}, " \
                                  f"Python x is: {px} (state, next = {pstate} {pnext})"
        assert dut.y.value == py, f"Output was incorrect on the {cycle}th (p={n_c})  cycle\n" \
                                  f"Inputs: {r}, {a}\n"\
                                  f"SV y is: {dut.y.value}, " \
                                  f"Python y is: {py} (state, next = {pstate} {pnext})"
```


## Results
![img](/Images/his.png)

