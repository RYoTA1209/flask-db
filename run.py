import sys
sys.path.append('./src')

from app import app
import models

if __name__ == '__main__':
    app.run(debug=True)
