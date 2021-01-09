import sys
sys.path.append('./src')

from app import app

if __name__ == '__main__':
    app.run(debug=True)
