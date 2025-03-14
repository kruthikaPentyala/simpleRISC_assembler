      mov r1, 1       // fact = 1
      mov r2, r0      // the number is stored in input port register r0
loop: 
      mul r1, r1, r2 // fact = fact * i
      sub r2, r2, 1   // decrement i
      cmp r2, 1       // compare i > 1
      bgt loop        // if i > 1 then remain in loop
      mov r3, r1      // else the result is stored in output port register r3
      hlt            // stops program counter to be incremented