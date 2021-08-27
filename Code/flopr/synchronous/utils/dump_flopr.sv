module dump();
	initial begin
	    $dumpfile ("flopr.vcd");
	    $dumpvars (0, flopr);
	    #1;
	end
endmodule
	
