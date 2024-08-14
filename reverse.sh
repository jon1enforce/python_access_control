pipdeptree --freeze --warn silence | grep -P '^[\w0-9-=.]+' > reverse.txt
python3 reverse.py
