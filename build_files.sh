# build_files.sh
echo "########## BUILD START ##########"
uname -a
python3.9 -m pip install --upgrade setuptools
python3.9 -m pip install -r requirements.txt

python3.9 manage.py makemigrations
python3.9 manage.py migrate

python3.9 manage.py collectstatic --noinput --clear
echo "########## BUILD END ##########"
