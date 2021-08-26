module dump();
	initial begin
	    $dumpfile ("fulladder2.vcd");
	    $dumpvars (0, fulladder2);
	    #1;
	end
endmodule
	
