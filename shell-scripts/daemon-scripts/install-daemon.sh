#!/bin/bash

sudo chmod u+x run-daemon.sh

sudo chmod u+x stop-daemon.sh

cd template

while read line; do
    eval echo "$line" >>kip-system.service
done <"kip-system_template.service"

sudo rm -f /etc/systemd/system/kip-system.service

sudo cp kip-system.service /etc/systemd/system/kip-system.service

rm -f kip-system.service

cd ..

sudo systemctl daemon-reload

# sudo systemctl start gideone-service.service

# sudo systemctl enable kip-system-service.service

cd ..
