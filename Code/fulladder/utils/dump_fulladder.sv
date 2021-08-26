module dump();
	initial begin
	    $dumpfile ("fulladder.vcd");
	    $dumpvars (0, fulladder);
	    #1;
	end
endmodule
	
