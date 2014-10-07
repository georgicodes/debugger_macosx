## What are they?
Debuggers are programs that control the application being debugged so that programmers can follow the flow of execution and even pause it to inspect program state. 

Underneath, debuggers are quite complex piecces of software that require knowledge of the inner workings of operating systems and the underlying CPU architecture.

## Who uses them?
Programmers use debuggers to find bugs in software but also hackers might use them to find vulnerabilites **FIX ME**

## How do they work?
There are different types of debuggers but the one we are going to focus on is source-level symbolic debugging. Source-level debugging symbolic debugging is the most common type of debugging and its the type of debugging you would see in Eclipse or IntelliJ where the high-level language source code like Java is displayed to the user as it is executed by the CPU. This is as opposed to stepping through machine instructions which would be of little help to to the end user. The deubgger actually maps the original source code directly to the machine code that is being executed.

### Breakpoints
Debuggers have the ability to pause the execution of a program by using breakpoints. There are both hardware and software breakpoints.

### Hardware
Some processors have hardware support for breakpoints. The type of processors on MacBook's are x86 which have support for breakpoints with debug registers that are used explicitly by debuggers.

### Software
Debuggers implement software breakpoints by replacing the instruction at the breakpoint's location so that the debugger is called instead.

Once a debugger hits a breakpoint it is possible to view the current stacktrace, the values in the hardware registers as well as the contents of the program's memory.

## Debugging Principles

### The Heisenberg Principle

## Stacks
An important feature of a debugger is to be able to view the stack. There is a seperate stack per thread and each frame on the stack represents a function call, also known as an activation record. Stacks grown downward from the highest address space to the lowest.

The debugger can either create the process to debug or attach to an already running process. The debugger will consult the symbol table which is contained in the executable being debugged. The symbol table is consulted in order to map between the source code and the byte code instructions.


## References
* [How Debuggers Work (book)]()
* [Gray Hat Python (book)](http://www.nostarch.com/ghpython.htm)
* [How Debuggers Work](http://www.alexonlinux.com/how-debugger-works)
* [x86 Architecture - Windows](http://msdn.microsoft.com/en-us/library/windows/hardware/ff561502(v=vs.85).aspx)


CPU View
- actual machine instructions, current register values, current hardware stack (from which software stack is discussed)


## Glossary
* thread
* global and local variables
* Dissassembly
* Registers
* x86
* breakpoint
* Heisenberg principle
