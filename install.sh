#!/bin/bash
# Django-peonHUB-Installer
# peondusud
echo "Django-peonHUB-Installer"
echo "by peondusud"
sleep 2
if [ $USER != root ]; then
echo "¡Is necessary be root!"
exit 0
fi

echo "[install python]"
aptitude install python

aptitude install unzip
echo "[install python-pip]"
aptitude install python-pip
echo "[install python-mysql]"
aptitude install python-mysql
echo "[install python-django]"
aptitude install python-django
echo "[install django]"
pip install django
echo "[install django extensions]"
pip install django-extensions


echo "[Downloadin peonHUB app]"
wget http://www.peondusud.org/peonHUB.zip
unzip peonHUB.zip


cd peonHUB/

echo "[please type python manage.py runserver]"
python manage.py syncdb