# encoding: utf-8

from service import app, PORT

if __name__ == '__main__':
    app.run(port=PORT, host='0.0.0.0')
