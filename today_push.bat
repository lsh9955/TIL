@echo off
a="# ("
b=$(date '+%Y.%m.%d')
c=")"
echo -e $a$b$c >> WHATILEARNED.py
git add .
git commit -m '%date%_commit'
git push origin master
timeout 4