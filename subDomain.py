#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import pyfiglet
import argparse
import sys
import time 
import random
import string
import paramiko
from datetime import datetime

#positional args

parser = argparse.ArgumentParser(description='tool use: amass')  # argumnt description
parser.add_argument(  # add argumnt
    '-b',
    '--brute-force',
    help='Brute force 2m wordlist',
    dest='brute',
    metavar='',
    )
parser.add_argument(  # add argumnt
    '-d',
    '--domain',
    help='Use All Tool',
    dest='dom',
    required='True',
    metavar='',
    )
parser.add_argument(  # add argumnt
    '-o',
    '--out-file',
    help='Default Save File: result/{data.time}.txt',
    metavar='',
    dest='file',
    required=False,
    )
args = parser.parse_args()

def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))
rando1 = randomString()
rando2 = randomString()
def slowprint(s):  # slow print
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1. / 1000)

ascii_banner = pyfiglet.figlet_format('SUB DOMAIN')  # art
ama = pyfiglet.figlet_format('amass')  # art
aqu = pyfiglet.figlet_format('aquatone')  # art
passh = pyfiglet.figlet_format('Passivehunter')  # art
subf = pyfiglet.figlet_format('SubFinder')  # art
subl = pyfiglet.figlet_format('sublist3r') # art
censys = pyfiglet.figlet_format('censys') # art
crtsh_enum_art = pyfiglet.figlet_format('crtsh_enum_psql') # art
bruteart = pyfiglet.figlet_format('brute') # art 
print(ascii_banner)

slowprint('----------------------')
slowprint('Sub Domain Enum!     -')
time_file = datetime.now().strftime('%F-%I:%M:%S')  # time
slowprint(time_file + '  -')
shr = '---------------------------------------------------'
res = '\n Result:'
print(shr)
check = ('.ac','.ad','.ae','land','.aero','.ag','.al','.am','.asia','.at','.az','.b','.be','.bg','.biz','.bo','.br','.bz','.ca','.cc','.cf','.ch','.cl','.cm','.cn','.co','.com','.cz','.de','.dk','.dz','.ec','.edu','.es','.eu','.fi','.fm','.fr','.ga','.gd','.gen','.gi','.gl','.go','.gob','.gov','.gr','.gs','.hk','.hr','.hu','.ie','.im','.in','.info','.int','.io','.iq','.ir','.is','.it','.jp','.kr','.kz','.la','.li','.lk','.lt','.lu','.lv','.ly','.md','.me','.mil','.mobi','.mp','.ms','.msk','.mus','.mx','.my','.ne','.net','.nhs','.nl','.no','.or','.org','.pe','.ph','.pl','.pn','.pt','.re','.ro','.rs','.ru','.sc','.se','.sg','.sh','.sk','.sm','.sn','.st','.su','.sx','.tk','.tl','.to','.tt','.tv','.ua','.uk','.us','.vc','.vn','.ws','.xxx')
domain = str(args.dom)
grep = " | grep '" + domain + "'"

if args.file:
    file = args.file
else:
    file = args.dom 

save = 'result/' + file
f=open(save,'a+')
amass = 'amass enum -d ' + domain + ' -o ' + 'result/' + file 
aquatone = 'aquatone-discover -d ' + domain 
aqufile = 'cat /home/abdalla/aquatone/'+domain+'/hosts.txt | cut -d "," -f 1 >> result/' + file
passhunt = 'python3 tool/Passivehunter/passivehunter.py ' + domain  + ' >> result/' + file
subfi = 'subfinder -d ' +  domain + ' -o ' + '.test/' + rando1
subfifile = 'cat ' + '.test/' + rando1 + ' >> result/' + file
sublist3r = 'python3 tool/Sublist3r/sublist3r.py -d ' + domain + ' -o .test/' + rando2
sublistfile = 'cat .test/' + rando2 + ' | awk \'BEGIN{FS="<BR>"} { for (i=2; i<=NF; i++) print $i }\' ' + '>> result/' + file  
subnum = 'python tool/subnum/script.py ' + domain + ' >> result/' + file
crtsh_enum_psql = 'python3 tool/the-art-of-subdomain-enumeration/crtsh_enum_psql.py ' + domain + ' >>' + 'result/'+ file
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('', username='', password='', key_filename='')
if domain:
    if domain.endswith(check) == False:
        print('ERROR: Pleas Check Domain')
    else:
        print(ama, shr, res) #amass
        os.system(amass)
        print('DONE...\n' + '--------------------------------------------------\n' + aqu, shr, res) #aquatone
        os.system(aquatone)
        os.system(aqufile)
        print('DONE...\n' + '--------------------------------------------------\n' + passh, shr, res) #passhunt
        os.system(passhunt)
        print('DONE...\n' + '--------------------------------------------------\n' + subf, shr, res) #subfinder
        os.system(subfi)
        os.system(subfifile)
        print('DONE...\n' + '--------------------------------------------------\n' + subl, shr, res) #sublist3r
        print(sublist3r)
        os.system(sublist3r)
        os.system(sublistfile)
        """
        print('DONE...\n' + '--------------------------------------------------\n' + censys, shr, res) #subnum
        os.system(subnum)
        """
        print('DONE...\n' + '--------------------------------------------------\n' + bruteart, shr, res) #brute
        print('sed -e \'s/$/.'+domain+'/\' SubDomainsEnum/jhaddix_commonspeak.txt > company_profile.txt | python SubDomainsEnum/MassForce.py SubDomainsEnum/company_profile.txt | grep \''+domain+'\' | cut -d " " -f 1')
        stdin, stdout, stderr = ssh.exec_command('sed -e \'s/$/.'+domain+'/\' SubDomainsEnum/jhaddix_commonspeak.txt > SubDomainsEnum/company_profile.txt ; python SubDomainsEnum/MassForce.py SubDomainsEnum/company_profile.txt | grep \''+domain+'\' | cut -d " " -f 1')
        exit_code = stdout.read().decode('ascii').strip("\n")
        f=open('result/'+file,'a+')
        f.write(exit_code)
        ssh.close()