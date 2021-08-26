# COCOTB variables
export COCOTB_REDUCED_LOG_FMT=1
export PYTHONPATH := test:$(PYTHONPATH)

flop:
	rm -rf bin/
	mkdir bin
	iverilog -o bin/flop.vvp -s flop -s dump -g2012 src/flop.sv utils/dump_flop.sv
	PYTHONOPTIMIZE=${NOASSERT} MODULE=test_flop vvp -M $$(cocotb-config --prefix)/cocotb/libs -m libcocotbvpi_icarus  bin/flop.vvp
	! grep failure results.xml

show_graph:
	gtkwave flop.vcd

synth:
	yosys -p "read_verilog -sv src/flop.sv; proc; opt; show -colors 2 -width -signed"

clean:
	rm -rf bin/
	rm -rf *.vcd
	rm -rf *.xml
	rm -rf __pycache__

.PHONY: clean

	
