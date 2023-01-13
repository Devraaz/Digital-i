echo "BUILD START"
python3.9 -m pip instal -r requiremnets.txt
python3.9 manage.py collectstatic --noinput --clear
echo "BUILD END"