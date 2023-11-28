from  filesystem import *
import subprocess



def main():
    # parser = argparse.ArgumentParser(description='SOC CIB generator minimal template from sn1per workspace.')
    # parser.add_argument('workspace', help='folder from workpace sn1per')

    # args = parser.parse_args()
    # workspace = args.workspace

    # conf = read_yaml("conf.yaml")

    # subprocess.run(["masscan", "Geeks for geeks"],
    #                  capture_output=True)

 #resolve dns-name 
 #cat hosts.txt | xargs -n1 -P100 dig +short +retry=3 | grep -E '^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}' > ip_list.txt

# masscan 95.181.129.248 -p0-65535 -oJ ~/masscan-altlib.json

# nmap -Pn -sS -iL /home/kali/altlib/nmap_ips.txt -p $(tr '\n' , </home/kali/altlib/nmap_ports.txt)  -A  -T5 –oJ /home/kali/altlib/nmap_report.json


# #curl -s https://crt.sh/?q=%25.$TARGET > $LOOT_DIR/domains/domains-$TARGET-presorted.txt
# #cat $LOOT_DIR/domains/domains-$TARGET-presorted.txt | grep $TARGET | grep TD | sed -e 's/<//g' | sed -e 's/>//g' | sed -e 's/TD//g' | sed -e 's/BR/\n/g' | sed -e 's/\///g' | sed -e 's/ //g' | sed -n '1!p' | grep -v "*" | sort -u > $LOOT_DIR/domains/domains-$TARGET-crt.txt

# # cat $LOOT_DIR/web/spider-$TARGET.txt 2> /dev/null | egrep -iE "$GREP_EXTENSIONS" | tee $LOOT_DIR/web/static-extensions-$TARGET.txt | head -n $GREP_MAX_LINES


# theHarvester -d altlib.ru -b all -f ~/altlib2 -v -t 
# blackwidow -d target.com -l 5 -s y  ### /usr/share/blackwidow/target.com
# #webtech -u http://$TARGET:$PORT --oj ~/web-tech-targe.json # https://github.com/ShielderSec/webtech/blob/master/webtech_example.py
# #wget --connect-timeout=5 --read-timeout=10 --tries=1 https://$TARGET/robots.txt -O ~/robots.txt 2> /dev/null
# wafw00f https://example.org -a -o ~/waf.json -f json


# # cat /usr/share/blackwidow/"$TARGET"_*/"$TARGET"_*-urls-sorted.txt > $LOOT_DIR/web/spider-$TARGET.txt 2>/dev/null

# # curl -sX GET "http://web.archive.org/cdx/search/cdx?url=*.$TARGET/*&output=text&fl=original&collapse=urlkey" | tee $LOOT_DIR/web/waybackurls-$TARGET.txt 2> /dev/null | head -n 250
# # cat $LOOT_DIR/web/waybackurls-$TARGET.txt 2> /dev/null >> $LOOT_DIR/web/spider-$TARGET.txt 2>/dev/null

# # curl -s GET "https://api.hackertarget.com/pagelinks/?q=http://$TARGET" | egrep -v "API count|no links found|input url is invalid|API count|no links found|input url is invalid|error getting links" | tee $LOOT_DIR/web/hackertarget-http-$TARGET.txt 2> /dev/null | head -n 250
# # cat $LOOT_DIR/web/hackertarget-*-$TARGET.txt 2> /dev/null >> $LOOT_DIR/web/spider-$TARGET.txt 2>/dev/null

# # curl -sX GET "http://index.commoncrawl.org/CC-MAIN-2022-33-index?url=*.$TARGET&output=json" -H 'Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Googlebot/2.1; +http://www.google.com/bot.html) Safari/537.36' 2> /dev/null | jq -r .url | egrep -v "null" | tee $LOOT_DIR/web/passivespider-$TARGET.txt 2> /dev/null | head -n 250
# # cat $LOOT_DIR/web/passivespider-$TARGET.txt 2> /dev/null >> $LOOT_DIR/web/spider-$TARGET.txt 2>/dev/null


# # gau -subs $TARGET | tee $LOOT_DIR/web/gua-$TARGET.txt 2> /dev/null | head -n 250
# # cat $LOOT_DIR/web/gua-$TARGET.txt 2> /dev/null >> $LOOT_DIR/web/spider-$TARGET.txt 2>/dev/null


main()