#!/bin/bash

sudo swapoff /swapfile

sudo rm /swapfile

sudo fallocate -l 20g /swapfile

sudo chmod 600 /swapfile

sudo mkswap /swapfile

sudo swapon /swapfile
