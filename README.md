grepSilon
=========

Tiny script for UNIX-like grepping blocks of text instead of lines.

Example use
===========
do an nmap scan for the heartbleed bug:

nmap -d --script ssl-heartbleed --script-args -sV X.X.X.X/24 > save.it.to.a.file

And then, you drop this in the shell:

python grepSilon.py "Service Info" "Risk factor: High" save.it.to.a.file | grep "Nmap scan report for " | awk '{ print $5 }'

And voilá, the vulnerable hosts are at your feet!

DISCLAIMER
==========
This is for educational purposes only. Any kind of unauthorized use is illegal. You know, it's never the sword's fault to harm the victim.

External links:
===============
How to use nmap for heartbleed scans: https://gist.github.com/bonsaiviking/10402038
