`timescale 1ns/1ps

//EX.A.34 Full Adder Using Nonblocking Assigments
// nonblocking assignments (not recommended)
module fulladder2(input logic a, b, cin,
                 output logic sum, cout);

    logic p, g;

    always_comb
        begin
            p <= a ^ b;  //nonblocking
            g <= a & b;  //nonblocking

            sum <= p ^ cin;
            cout <= g | (p & cin);
        end
endmodule