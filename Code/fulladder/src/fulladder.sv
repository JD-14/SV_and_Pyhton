`timescale 1ns/1ps

//EX.A.8 Full Adder
module fulladder(input logic a, b, cin,
                 output logic sum, cout);

    logic p, g;

    assign p = a ^ b;
    assign g = a & b;

    assign sum = p ^ cin;
    assign cout = g | (p & cin);
endmodule
