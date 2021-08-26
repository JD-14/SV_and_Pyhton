`timescale 1ns/1ps

//Ex.A.20 Register
module flop
       #(parameter w = 2)
       (input logic clk,
       input logic [w-1:0] d,
       output logic [w-1:0] q);

       always_ff @(posedge clk)
        q <= d;
endmodule
	
