#!/bin/sh

kill -9 $(cat /var/run/temperature_pid) >/dev/null 2>&1
