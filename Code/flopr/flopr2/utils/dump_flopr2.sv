module dump();
	initial begin
	    $dumpfile ("flopr2.vcd");
	    $dumpvars (0, flopr2);
	    #1;
	end
endmodule
	
