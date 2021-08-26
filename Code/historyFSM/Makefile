# COCOTB variables
export COCOTB_REDUCED_LOG_FMT=1
export PYTHONPATH := test:$(PYTHONPATH)

historyFSM:
	rm -rf bin/
	mkdir bin
	iverilog -o bin/historyFSM.vvp -s historyFSM -s dump -g2012 src/historyFSM.sv utils/dump_historyFSM.sv
	PYTHONOPTIMIZE=${NOASSERT} MODULE=test_historyFSM vvp -M $$(cocotb-config --prefix)/cocotb/libs -m libcocotbvpi_icarus  bin/historyFSM.vvp
	! grep failure results.xml

show_graph:
	gtkwave historyFSM.vcd

synth:
	yosys -p "read_verilog -sv src/historyFSM.sv; proc; opt; show -colors 2 -width -signed"

clean:
	rm -rf bin/
	rm -rf *.vcd
	rm -rf *.xml
	rm -rf __pycache__

.PHONY: clean

	
