#
# Conteudo do arquivo `wsgi.py`
#
import sys

sys.path.insert(0, "/var/www/html/projetos/flask-test")

from myapp import app as application
