import cocotb
from cocotb.triggers import Timer
from model.fulladder_model import fulladder
import random

@cocotb.test()
async def fulladder_constant_tb(dut):
    a = 1
    b = 1
    c = 1
    dut.a <= a
    dut.b <= b
    dut.cin <= c

    await Timer(2, units='ns')

    psum, pcout = fulladder(a, b, c)  #Python adder
    assert dut.sum.value == psum, f"Adder result is incorrect:\n" \
                                  f"SV sum is: {dut.sum.value}, " \
                                  f"Python sum is : {psum}"
    assert dut.cout.value == pcout, f"Adder result is incorrect:\n" \
                                    f"SV cout is: {dut.cout.value}, " \
                                    f"Python cout is : {pcout}"

@cocotb.test()
async def fulladder_random_tb(dut):
    for i in range(20):
        a = random.randint(0, 1)
        b = random.randint(0, 1)
        c = random.randint(0,1)
        dut.a <= a
        dut.b <= b
        dut.cin <= c

        await Timer(2, units='ns')

        cycle = i+1
        psum, pcout = fulladder(a, b, c) #Python adder
        assert dut.sum.value == psum, f"output was incorrect on the {cycle}th cycle:\n" \
                                      f"SV sum is: {dut.sum.value}, " \
                                      f"Python sum is : {psum}"
        assert dut.cout.value == pcout, f"output was incorrect on the {cycle}th cycle:\n" \
                                        f"SV cout is: {dut.cout.value}, " \
                                        f"Python sum is : {pcout}"