MaomiHzBot
===============

It's just another simple Telegram bot. Chat to `@MaomiHzBot <https://t.me/maomihzbot>`_ on Telegram!

================
Introduction
================

The bot is based on ``python-telegram-bot`` and ``flask``, and can be deployed to any WSGL-compatible server. Note that in order to set a webhook, you need and valid SSL certificate. If you use a self-signed certificate you have to upload to Telegram manually, and the build-in web interface does not support uploading certificate.

=======
Deploy
=======

The program is based on flask and python. Python 3 and virtualenv is recommend. Only Python 3 can correctly handle CJK characters.

First, clone the project::

  git clone https://github.com/maomihz/MaomiHzBot
  cd MaomiHzBot

Setup python 3 virtualenv and activate::

  python3 -m virtualenv venv
  source venv/bin/activate

Install all the dependencies::

  pip install -r requirements.txt

Install itself::

  pip install -e .

When you register your bot, you should get a bot token. Export the token as an environment variable::

  export TOKEN=123456789:AABBccDDDeeFFgHiJJkL1234mmNo56P7qRS

Setup flask environment variable::

  export FLASK_APP=maomihzbot

Start the flask server::

  flask run

By default, the server would be started on 127.0.0.1:5000. You might need to set up an HTTP proxy that support https to make the bot work. For more deployment options, see `Deploying <http://flask.pocoo.org/docs/0.12/deploying/>`_.

================
Register Webhook
================

Once the server is started, navigate to https://yoururl.example.com/webhook. Fill in your server address starting with https:// and your bot token (for security reason). Your webhook URL should look like this::

  https://yoururl.example.com/bot123456789:AABBccDDDeeFFgHiJJkL1234mmNo56P7qRS

=================
More Settings
=================

To enable the /fortune command, fill text into maomihzbot/txt/fortune.txt, one line a time. Each line is a fortune and would be randomly selected.

By default, /help and /start is in Chinese. Modify maomihzbot/txt/help.txt and maomihzbot/txt/start.txt to change the reply text.

If you want to forward all text messages to a user or an channel, set the environment variable ``BROADCAST_ID``::

  export BROADCAST_ID=@yourchannel

For a channel the ID should start with @, and for a user the id should be a number. 

=====================
Copyright
=====================
  The MIT License (MIT)

  Copyright (c) 2017 Dexter MaomiHz

  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

  The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
