pipdeptree --freeze --warn silence | grep -P '^[\w0-9-=.]+' > reverse.txt
#pipdeptree --freeze --warn silence --local-only --reverse | grep -P '^[\w0-9-=.]+' > reverse.txt
sudo python3 -Xfrozen_modules=off  reverse.py
