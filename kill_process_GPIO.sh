#!/usr/bin/env bash

pid_of_GPIO18="$(ps -ef|awk '$9=="GPIO18_Blinking.py"{print $2}')"
kill ${pid_of_GPIO18}
echo "Stoping Blinking LED 18 code with PID=${pid_of_GPIO18}"

pid_of_GPIO23="$(ps -ef|awk '$9=="GPIO23_Blinking.py"{print $2}')"
kill ${pid_of_GPIO23}
echo "Stoping Blinking LED 23 code with PID=${pid_of_GPIO23}"

