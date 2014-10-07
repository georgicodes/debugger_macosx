#!/usr/bin/python

#----------------------------------------------------------------------
# Be sure to add the python path that points to the LLDB shared library.
# On MacOSX csh, tcsh:
#   setenv PYTHONPATH /Applications/Xcode.app/Contents/SharedFrameworks/LLDB.framework/Resources/Python
# On MacOSX sh, bash:
#   export PYTHONPATH=/Applications/Xcode.app/Contents/SharedFrameworks/LLDB.framework/Resources/Python
#----------------------------------------------------------------------

import lldb
import os
import lldbutil
# from lldbutil import print_stacktrace


def disassemble_instructions(insts):
    for i in insts:
        print i

# Set the path to the executable to debug
exe = "./debuggee/a.out"

# Create a new debugger instance
debugger = lldb.SBDebugger.Create()

# When we step or continue, don't return from the function until the process
# stops. Otherwise we would have to handle the process events ourselves which, while doable is
#a little tricky.  We do this by setting the async mode to false.
debugger.SetAsync (True)

# Create a target from a file and arch
print "Creating a target for '%s'" % exe

target = debugger.CreateTargetWithFileAndArch (exe, lldb.LLDB_ARCH_DEFAULT)
# attach_info = lldb.SBAttachInfo (64925)
# target = debugger.FindTargetWithProcessID(64925)

if target:
  print "Target process created."
  error = lldb.SBError()
  # If the target is valid set a breakpoint at main
  # main_bp = target.BreakpointCreateByName ("main", target.GetExecutable().GetFilename());

  # print main_bp

  # Launch the process. Since we specified synchronous mode, we won't return
  # from this function until we hit the breakpoint at main
  process = target.LaunchSimple (None, None, os.getcwd())
  # process = target.Attach (attach_info, error)

  # Make sure the launch went ok
  if process:
      # Print some simple process info
      state = process.GetState()
      print "Process info %s" % process

      for thread in process:
          ID = thread.GetThreadID()
          print "thread id: %d" % ID
          frames = thread.frames
          for frame in frames:
            print frame
            registers = lldbutil.get_GPRs(frame)
            for reg in registers:
              print "%s => %s" % (reg.GetName(), reg.GetValue())


          # if thread.GetStopReason() == lldb.eStopReasonBreakpoint:
          #     stopped_due_to_breakpoint = True
          # for frame in thread:
          #     self.assertTrue(frame.GetThread().GetThreadID() == ID)
          #     if self.TraceOn():
          #         print frame

