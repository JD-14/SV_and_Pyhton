# COCOTB variables
export COCOTB_REDUCED_LOG_FMT=1
export PYTHONPATH := test:$(PYTHONPATH)

fulladder:
	rm -rf bin/
	mkdir bin
	iverilog -o bin/fulladder.vvp -s fulladder -s dump -g2012 src/fulladder.sv utils/dump_fulladder.sv
	PYTHONOPTIMIZE=${NOASSERT} MODULE=test_fulladder vvp -M $$(cocotb-config --prefix)/cocotb/libs -m libcocotbvpi_icarus  bin/fulladder.vvp
	! grep failure results.xml

show_graph:
	gtkwave fulladder.vcd

synth:
	yosys -p "read_verilog -sv src/fulladder.sv; proc; opt; show -colors 2 -width -signed"

clean:
	rm -rf bin/
	rm -rf *.vcd
	rm -rf *.xml
	rm -rf __pycache__

.PHONY: clean

	
