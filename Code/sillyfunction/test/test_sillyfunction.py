import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer
from model.sillyfunction_model import sillyfunction
from cocotb.triggers import RisingEdge, FallingEdge, ClockCycles
import random

@cocotb.test()
async def silly_constant_tb(dut):
    a = 1
    b = 0
    c = 1
    dut.a <= a
    dut.b <= b
    dut.c <= c

    await Timer(2, units='ns')

    py = sillyfunction(a, b, c)
    assert dut.y.value == py, f"Result is incorrect: \n"\
                              f"Sv y is: {dut.y.value}, "\
                              f"Python y is: {py}"

@cocotb.test()
async def silly_random_tb(dut):
    for i in range(8):
        a = random.randint(0, 1)
        b = random.randint(0, 1)
        c = random.randint(0,1)
        dut.a <= a
        dut.b <= b
        dut.c <= c

        await Timer(2, units='ns')

        cycle = i+1
        py = sillyfunction(a, b, c)
        assert dut.y.value == py, f"Randomised test failed on the {cycle}th cycle\n" \
                                                      f"Sv y is: {dut.y.value}, " \
                                                      f"Python y is: {py}"