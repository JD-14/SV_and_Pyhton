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