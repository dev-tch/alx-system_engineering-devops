#!/usr/bin/env bash
time=$(date +%s)
conf_ufw="/etc/ufw/before.rules"
bkp_conf_ufw="${conf_ufw}_${time}.bkp"

CONF="# firewall redirects port 8080/TCP to port 80/TCP\n*nat\n:PREROUTING ACCEPT [0:0]\n-A PREROUTING -p tcp --dport 8080 -j REDIRECT --to-port 80\nCOMMIT"

# Check if conf_ufw contains the specific string
if ! sudo grep -q "# firewall redirects port 8080" "$conf_ufw"; then
    echo "The specific string is present in $conf_ufw. Proceeding with the script."

    # Continue with the rest of the script
    sudo cp "$conf_ufw" "$bkp_conf_ufw"
    sudo awk -v conf="$CONF" '/^[^#]/ && !inserted { print conf; inserted=1 } 1' "$conf_ufw" > temp_file && sudo mv temp_file "$conf_ufw"
    sudo ufw reload

else
    echo "The specific string is not present in $conf_ufw. Exiting without making changes."
fi

