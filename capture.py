class TestCommand(GenericCommand):
    """ New Test Command"""
    _cmdline_ = "testcmd"
    _syntax_  = f"{_cmdline_}"

    @only_if_gdb_running
    def do_invoke(self, argv):
        # Print some info about the architecture of the environment
        print(f"get.arch={gef.arch}")

        frame = gdb.selected_frame()
        rdi_reg = frame.read_register("rdi")
        r15_reg = frame.read_register("r15")
        print(f"get.rdi={rdi_reg}")
        print(f"get_r15={r15_reg}")
        # Print some info about the current $pc
        print(f"get.arch.pc={gef.arch.pc:#x}")
        print(f"get.x86_registers={X86_64.all_registers}")
        registers = X86_64.all_registers
        for reg in registers:
            reg_data = frame.read_register(reg[1:])
            print(f"get.{reg} = {reg_data}")
        # regs = Architecture.registers

# register_external_command(TestCommand())


class Print_X86_64_Registers(GenericCommand):
    """ Command to Print Values of x86 Registers To stdout """
    _cmdline_ = "print_registers_x86"
    _syntax_  = f"{_cmdline_}"

    @only_if_gdb_running
    def do_invoke(self,argv):
        frame = gdb.selected_frame()

        print("Register Values:")
        registers = X86_64.all_registers
        for reg in registers:
            # read_register does not like the '$' at the beginning of the register name
            reg_data = frame.read_register(reg[1:])
            print(f"{reg} -> {reg_data}")


class Get_Current_Instruction(GenericCommand):
    """ Command to Print the Current Instruction to stdout """
    _cmdline_ = "get_current_instruction"
    _syntax_  = "{_cmdline_}"

    @only_if_gdb_running
    def do_invoke(self, argv):
       frame = gdb.selected_frame()
       arch = frame.architecture()
       insts = arch.disassemble(gef.arch.pc)
       inst = insts[0]
       addr = inst["addr"]
       assem = inst["asm"]
       print(f"instruction address: {addr:#x}")
       print(f"instruction assembly: {assem}")


class StartProgram(GenericCommand):
    """ Command to begin running the loaded program """
    _cmdline_ = "start_program"
    _syntax_  = "{_cmdline_}"

    def do_invoke(self, argv):
        gdb.execute("r")

class StepInstruction(GenericCommand):
    """ Command to single step the program """
    _cmdline_ = "step_instruction"
    _syntax_  = "{_cmdline_}"

    def do_invoke(self, argv):
        gdb.execute("si")

register_external_command(TestCommand())
register_external_command(Print_X86_64_Registers())
register_external_command(Get_Current_Instruction())
register_external_command(StartProgram())
register_external_command(StepInstruction())






