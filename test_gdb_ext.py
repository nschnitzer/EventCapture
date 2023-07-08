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

register_external_command(TestCommand())
