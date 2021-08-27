# COCOTB variables
export COCOTB_REDUCED_LOG_FMT=1
export PYTHONPATH := test:$(PYTHONPATH)

flopr2:
	rm -rf bin/
	mkdir bin
	iverilog -o bin/flopr2.vvp -s flopr2 -s dump -g2012 src/flopr2.sv utils/dump_flopr2.sv
	PYTHONOPTIMIZE=${NOASSERT} MODULE=test_flopr2 vvp -M $$(cocotb-config --prefix)/cocotb/libs -m libcocotbvpi_icarus  bin/flopr2.vvp
	! grep failure results.xml

show_graph:
	gtkwave flopr2.vcd

synth:
	yosys -p "read_verilog -sv src/flopr2.sv; proc; opt; show -colors 2 -width -signed"

clean:
	rm -rf bin/
	rm -rf *.vcd
	rm -rf *.xml
	rm -rf __pycache__

.PHONY: clean

	
