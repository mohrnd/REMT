#!/bin/bash

/sbin/shutdown "$@"

# the issue here is since we created a new symbolic link, the script shutdown_terminal.py keeps being executed over and over
