echo -e "$OKRED ╔═╗╦═╗╔╦╗╔═╗╦ ╦$RESET"
echo -e "$OKRED ║  ╠╦╝ ║ ╚═╗╠═╣$RESET"
echo -e "$OKRED ╚═╝╩╚═ ╩o╚═╝╩ ╩$RESET"
echo -e "${OKGREEN}====================================================================================${RESET}•x${OKGREEN}[`date +"%Y-%m-%d](%H:%M)"`${RESET}x•"
echo -e "$OKRED GATHERING CERTIFICATE SUBDOMAINS $RESET"
echo -e "${OKGREEN}====================================================================================${RESET}•x${OKGREEN}[`date +"%Y-%m-%d](%H:%M)"`${RESET}x•"
echo -e "$RESET"
curl -s https://crt.sh/?q=%25.$TARGET > $LOOT_DIR/domains/domains-$TARGET-presorted.txt
cat $LOOT_DIR/domains/domains-$TARGET-presorted.txt | grep $TARGET | grep TD | sed -e 's/<//g' | sed -e 's/>//g' | sed -e 's/TD//g' | sed -e 's/BR/\n/g' | sed -e 's/\///g' | sed -e 's/ //g' | sed -n '1!p' | grep -v "*" | sort -u > $LOOT_DIR/domains/domains-$TARGET-crt.txt
wc -l $LOOT_DIR/domains/domains-$TARGET-crt.txt 2> /dev/null
echo ""
echo -e "${OKRED}[+] Domains saved to: $LOOT_DIR/domains/domains-$TARGET-crt.txt"

echo -e "${OKGREEN}====================================================================================${RESET}•x${OKGREEN}[`date +"%Y-%m-%d](%H:%M)"`${RESET}x•"
echo -e "$OKRED GATHERING THEHARVESTER OSINT INFO $RESET"
echo -e "${OKGREEN}====================================================================================${RESET}•x${OKGREEN}[`date +"%Y-%m-%d](%H:%M)"`${RESET}x•"
cp -f /etc/theHarvester/api-keys.yaml ~/api-keys.yaml 2> /dev/null
cd ~ 2> /dev/null
theHarvester -d $TARGET -b all 2> /dev/null | tee $LOOT_DIR/osint/theharvester-$TARGET.txt 2> /dev/null 
cd $INSTALL_DIR 2> /dev/null
if [[ "$SLACK_NOTIFICATIONS_THEHARVESTER" == "1" ]]; then
	/bin/bash "$INSTALL_DIR/bin/slack.sh" postfile "$LOOT_DIR/osint/theharvester-$TARGET.txt"
fi

echo -e "${OKGREEN}====================================================================================${RESET}•x${OKGREEN}[`date +"%Y-%m-%d](%H:%M)"`${RESET}x•"
echo -e "$OKRED RUNNING ACTIVE WEB SPIDER & APPLICATION SCAN $RESET"
echo -e "${OKGREEN}====================================================================================${RESET}•x${OKGREEN}[`date +"%Y-%m-%d](%H:%M)"`${RESET}x•"
touch $LOOT_DIR/web/spider-$TARGET.txt 2>/dev/null
cp $LOOT_DIR/web/spider-$TARGET.txt $LOOT_DIR/web/spider-$TARGET.bak 2>/dev/null
blackwidow -u http://$TARGET:80 -l 3 -v n
cp -f /usr/share/blackwidow/"$TARGET"_80/"$TARGET"_80-*.txt $LOOT_DIR/web/ 2>/dev/null 
cat /usr/share/blackwidow/"$TARGET"_*/"$TARGET"_*-urls-sorted.txt > $LOOT_DIR/web/spider-$TARGET.txt 2>/dev/null
cat $LOOT_DIR/web/waybackurls-$TARGET.txt 2> /dev/null >> $LOOT_DIR/web/spider-$TARGET.txt 2>/dev/null
cat $LOOT_DIR/web/hackertarget-*-$TARGET.txt 2> /dev/null >> $LOOT_DIR/web/spider-$TARGET.txt 2>/dev/null
cat $LOOT_DIR/web/passivespider-$TARGET.txt 2> /dev/null >> $LOOT_DIR/web/spider-$TARGET.txt 2>/dev/null
cat $LOOT_DIR/web/gua-$TARGET.txt 2> /dev/null >> $LOOT_DIR/web/spider-$TARGET.txt 2>/dev/null
sed -ir "s/</\&lh\;/g" $LOOT_DIR/web/spider-$TARGET.txt 2>/dev/null
mv -f $LOOT_DIR/web/spider-$TARGET.txtr $LOOT_DIR/web/spider-$TARGET.txt 2>/dev/null
sort -u $LOOT_DIR/web/spider-$TARGET.txt 2>/dev/null > $LOOT_DIR/web/spider-$TARGET.sorted 2>/dev/null
mv $LOOT_DIR/web/spider-$TARGET.sorted $LOOT_DIR/web/spider-$TARGET.txt 2>/dev/null
diff $LOOT_DIR/web/spider-$TARGET.bak $LOOT_DIR/web/spider-$TARGET.txt 2> /dev/null | grep "> " 2> /dev/null | awk '{print $2}' 2> /dev/null > $LOOT_DIR/web/spider-new-$TARGET.txt

if [[ $(wc -c $LOOT_DIR/web/spider-new-$TARGET.txt | awk '{print $1}') > 3 ]]; then
    echo "[sn1persecurity.com] •?((¯°·._.• Spider URL change detected on $TARGET (`date +"%Y-%m-%d %H:%M"`) •._.·°¯))؟•" >> $LOOT_DIR/scans/notifications_new.txt
    head -n 20 $LOOT_DIR/web/spider-new-$TARGET.txt 2> /dev/null >> $LOOT_DIR/scans/notifications_new.txt 2> /dev/null
fi

cat $LOOT_DIR/web/spider-$TARGET.txt 2> /dev/null | egrep -iE "$GREP_EXTENSIONS" | tee $LOOT_DIR/web/static-extensions-$TARGET.txt | head -n $GREP_MAX_LINES

if [[ "$WEBTECH" = "1" ]]; then
    echo -e "${OKGREEN}====================================================================================${RESET}•x${OKGREEN}[`date +"%Y-%m-%d](%H:%M)"`${RESET}x•"
    echo -e "$OKRED GATHERING WEB FINGERPRINT $RESET"
    echo -e "${OKGREEN}====================================================================================${RESET}•x${OKGREEN}[`date +"%Y-%m-%d](%H:%M)"`${RESET}x•"
    webtech -u http://$TARGET:$PORT | grep \- | cut -d- -f2- | tee $LOOT_DIR/web/webtech-$TARGET-http-port$PORT.txt
fi

wget --connect-timeout=5 --read-timeout=10 --tries=1 https://$TARGET/robots.txt -O $LOOT_DIR/web/robots-$TARGET-https.txt 2> /dev/null
