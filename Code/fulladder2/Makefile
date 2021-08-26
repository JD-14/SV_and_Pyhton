# COCOTB variables
export COCOTB_REDUCED_LOG_FMT=1
export PYTHONPATH := test:$(PYTHONPATH)

fulladder2:
	rm -rf bin/
	mkdir bin
	iverilog -o bin/fulladder2.vvp -s fulladder2 -s dump -g2012 src/fulladder2.sv utils/dump_fulladder2.sv
	PYTHONOPTIMIZE=${NOASSERT} MODULE=test_fulladder2 vvp -M $$(cocotb-config --prefix)/cocotb/libs -m libcocotbvpi_icarus  bin/fulladder2.vvp
	! grep failure results.xml

show_graph:
	gtkwave fulladder2.vcd

synth:
	yosys -p "read_verilog -sv src/fulladder2.sv; proc; opt; show -colors 2 -width -signed"

clean:
	rm -rf bin/
	rm -rf *.vcd
	rm -rf *.xml
	rm -rf __pycache__

.PHONY: clean

	
