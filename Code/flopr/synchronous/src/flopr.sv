`timescale 1ns/1ps

//Ex.A.21 Resettable Register (Synchronous reset)
module flopr
       #(parameter w = 2)
       (input logic clk,
       input logic reset,
       input logic [w-1:0] d,
       output logic [w-1:0] q);

       // Synchronous reset
       always_ff @(posedge clk)
        if (reset) q <= 2'b0;       //using 2 bits
        else q <= d;
endmodule
