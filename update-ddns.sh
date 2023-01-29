#! /bin/bash

source .env

if [ -z $DDNS_USER ] || [ -z $DDNS_PASSWD ]; then
    echo "DDNS login details not set!"
    exit 1
fi


AGENT=None Website/None chlorinerickets@gmail.com
ADDR=dynupdate.no-ip.com/nic/update
WEBSITE=hamiltonroad.ddns.net
curl -A $AGENT "https://${DDNS_USER}:${DDNS_PASSWD}@${ADDR}?hostname=${WEBSITE}"
