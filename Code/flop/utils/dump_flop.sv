module dump();
	initial begin
	    $dumpfile ("flop.vcd");
	    $dumpvars (0, flop);
	    #1;
	end
endmodule
	
