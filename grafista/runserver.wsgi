import sys

print(sys.version)

activate_this = '/data/venv/bin/activate_this.py'

exec(open(activate_this).read(), dict(__file__=activate_this))

sys.path.append('/data/git/grafista/grafista/')

from application.main import app as application


if __name__ == '__main__':
    application.run()
