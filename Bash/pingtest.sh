#!/bin/bash

echo "Enter a website or IP to ping:"
read target

ping -c 4 $target
