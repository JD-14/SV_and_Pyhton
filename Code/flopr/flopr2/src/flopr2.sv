`timescale 1ns/1ps

//Ex.A.21 Resettable Register (Asynchronous reset)
module flopr2
       #(parameter w = 2)
       (input logic clk,
       input logic reset,
       input logic [w-1:0] d,
       output logic [w-1:0] q);

       // Asynchronous reset (clock should be positive, and reset negative to avoid error) [eventriger]
       always_ff @(posedge clk, posedge reset)
        if (reset) q <= 2'b0;       //using 2 bits
        else q <= d;
endmodule