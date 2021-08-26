`timescale 1ns/1ps

//EX.A.1 Combinational Logic
module sillyfunction(input logic a,b, c,
                     output logic y);

    assign y = ~a & ~b & ~c |
    	        a & ~b & ~c |
    		    a & ~b &  c ;
endmodule
	
