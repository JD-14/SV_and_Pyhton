import cocotb
from cocotb.clock import Clock
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
