#!/usr/bin/env bash

## Created by bigBear I just adjusted to match my setup ##

# Get the LAN IP address
lan_ip=$(hostname -I | awk '{print $1}')

# Backup the original config.php file
cp /mnt/Wolf8tbHdd1/data/nextcloud/config/config.php /mnt/Wolf8tbHdd1/data/nextcloud/config/config.php.bak

# Add the LAN IP to the config.php file
awk -v ip="$lan_ip" '/0 => '\''localhost'\''/{print; print "    1 => '\''"ip"'\'',"; next}1' /mnt/Wolf8tbHdd1/data/nextcloud/config/config.php.bak > /mnt/Wolf8tbHdd1/data/nextcloud/config/config.php

# Get the path to the docker-compose.yml file
COMPOSE_FILE="/var/lib/casaos/apps/nextcloud/docker-compose.yml"

# Apply changes using casaos-cli
casaos-cli app-management apply "nextcloud" --file="$COMPOSE_FILE"