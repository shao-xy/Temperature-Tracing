#!/bin/bash

cwd="$(dirname $0)"

if test $(id -u) -ne 0; then
    >&2 echo "Must be ROOT to install!"
    exit 1
fi

set -x
cp "${cwd}/systemd/temperature-tracer.service" /usr/lib/systemd/system/
systemctl enable temperature-tracer.service
