import cocotb
from cocotb.triggers import Timer
from model.gates_model import gates
import random

@cocotb.test()
async def gates_constant_tb(dut):
    a = 2
    b = 2
    dut.a <= a
    dut.b <= b

    await Timer(2, units='ns')

    y1, y2, y3, y4, y5 = gates(a, b) #Python Outputs
    assert dut.y1.value == y1, f"AND gate result is incorrect: {dut.y1.value}, " \
                               f"AND python output is: {y1}"
    assert dut.y2.value == y2, f"OR gate result is incorrect: {dut.y2.value}, " \
                               f"OR python output is: {y2}"
    assert dut.y3.value == y3, f"XOR gate result is incorrect: {dut.y3.value}, " \
                               f"XOR python output is: {y3}"
    assert dut.y4.value == y4, f"NAND gate result is incorrect: {dut.y4.value}, " \
                               f"NAND python output is: {y4}"
    assert dut.y5.value == y5, f"NOR gate result is incorrect: {dut.y5.value}, " \
                               f"NOR python output is: {y5}"


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