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

Before deploying, you should have a Telegram bot. If you do not have one, talk to `@Botfather <https://t.me/botfather>`_ on Telegram to get one. Once you register a bot, you will have a authorization token thant you'll need. The token looks like this::

  123456789:AABBccDDDeeFFgHiJJkL1234mmNo56P7qRS

The program is based on flask and python. Python 3 is recommend, and is the version tested. It is not guarenteed to work on Python 2, mainly because how it handles CJK characters.

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

Export the bot token as an environment variable::

  export TOKEN=123456789:AABBccDDDeeFFgHiJJkL1234mmNo56P7qRS

Setup flask environment variable::

  export FLASK_APP=maomihzbot

Start the flask server::

  flask run

By default, the server would be started on 127.0.0.1:5000. You might need to set up an HTTP proxy that support https to make the bot work. For more deployment options, see `Deploying <http://flask.pocoo.org/docs/0.12/deploying/>`_.

=====================
Deploying to Heroku
=====================

The project contains all files needed to deploy the app to `Heroku <https://www.heroku.com/>`_. Heroku offers a free plan and comes with an SSL certificate. You need an account on Heroku, and it's recommended to install the ``heroku`` command line tool to manage accounts.

Login to your heroku account::

  heroku login

Create a project (choose a unique name to replace ``example-app``)::

  heroku apps:create example-app

Add heroku remote::

  heroku git:remote -a example-app

Make some changes and commit with git, then push to the heroku remote address::

  git push heroku master

The app would be available at https://example-app.herokuapp.com. Read the next section for how to register webhook. 

================
Register Webhook
================

Once the server is started, navigate to https://yoururl.example.com/webhook. Fill in your server address starting with https:// and your bot token (for security reason). Your webhook URL should look like this::

  https://yoururl.example.com/bot123456789:AABBccDDDeeFFgHiJJkL1234mmNo56P7qRS

=================
More Settings
=================

To enable the ``/fortune`` command, fill text into ``maomihzbot/txt/fortune.txt``, one line a time. Each line is a fortune and would be randomly selected.

By default, ``/help`` and ``/start`` are in Chinese. Modify ``maomihzbot/txt/help.txt`` and ``maomihzbot/txt/start.txt`` to change the reply text.

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
