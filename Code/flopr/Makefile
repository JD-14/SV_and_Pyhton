# COCOTB variables
export COCOTB_REDUCED_LOG_FMT=1
export PYTHONPATH := test:$(PYTHONPATH)

flopr:
	rm -rf bin/
	mkdir bin
	iverilog -o bin/flopr.vvp -s flopr -s dump -g2012 src/flopr.sv utils/dump_flopr.sv
	PYTHONOPTIMIZE=${NOASSERT} MODULE=test_flopr vvp -M $$(cocotb-config --prefix)/cocotb/libs -m libcocotbvpi_icarus  bin/flopr.vvp
	! grep failure results.xml

show_graph:
	gtkwave flopr.vcd

synth:
	yosys -p "read_verilog -sv src/flopr.sv; proc; opt; show -colors 2 -width -signed"

clean:
	rm -rf bin/
	rm -rf *.vcd
	rm -rf *.xml
	rm -rf __pycache__

.PHONY: clean

	
