module dump();
	initial begin
	    $dumpfile ("historyFSM.vcd");
	    $dumpvars (0, historyFSM);
	    #1;
	end
endmodule
	
