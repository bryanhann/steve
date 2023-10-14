#!/bin/bash
[ "${MAGIC_PID}" == "" ] && export MAGIC_PID=$$
exit () {
    [ ! "${MAGIC_PID}" == "$$" ] && builtin exit
    echo try: builtin exit
}
