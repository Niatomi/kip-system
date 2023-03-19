#!/bin/bash

total_ram() {

    local totalram=$(cat /proc/meminfo | grep -i 'memtotal' | grep -o '[[:digit:]]*')

    echo $totalram

}

ram_size=$(total_ram)

required_min_ram_size=10000000

if [ $ram_size -le $required_min_ram_size ]; then

    echo "With total size of $ram_size kB it also may some problems to excecute scripts"

    echo "Add swap space"

    sudo chmod +x add-sawp-space.sh

    ./add-sawp-space.sh

fi
