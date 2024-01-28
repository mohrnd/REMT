read last line of the log file:
tac Shutdown.log | head -n 1

well i found a solution, i can just rename the /sbin/shutdown to something else then i can make an alias for shutdown

here are the diff options for shutdown and reboot:

Shut down the system.
Options:
     --help      Show this help
  -H --halt      Halt the machine
  -P --poweroff  Power-off the machine
  -r --reboot    Reboot the machine
  -h             Equivalent to --poweroff, overridden by --halt
  -k             Don't halt/power-off/reboot, just send warnings
     --no-wall   Don't send wall message before halt/power-off/reboot
  -c             Cancel a pending shutdown
     --show      Show pending shutdown

Reboot the system.
Options:
     --help      Show this help
     --halt      Halt the machine
  -p --poweroff  Switch off the machine
     --reboot    Reboot the machine
  -f --force     Force immediate halt/power-off/reboot
  -w --wtmp-only Don't halt/power-off/reboot, just write wtmp record
  -d --no-wtmp   Don't write wtmp record
     --no-wall   Don't send wall message before halt/power-off/reboot

See the halt(8) man page for details.
