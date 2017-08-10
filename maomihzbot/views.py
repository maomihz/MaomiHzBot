from flask import request, render_template, flash, url_for, redirect
from maomihzbot import app, bot, TOKEN


@app.route('/')
def index():
    return 'Hello, world!'


@app.route('/webhook', methods=['GET', 'POST'])
def set_webhook():
    if request.method == 'GET':
        return render_template('webhook.html')
    elif request.method == 'POST':
        url = request.form.get('url')
        token = request.form.get('token')
        if not url or not token:
            content = 'Please specify url and bot token. '
        elif not url.startswith('https://'):
            content = 'URL Must start with https:// !'
        elif token != TOKEN:
            content = 'Unauthorized!'
        else:
            if not url.endswith('/'):
                url = url + '/'
            hook = url + 'bot' + token
            try:
                bot.set_webhook(hook)
            except Exception as e:
                content = str(e)
            else:
                content = 'Webhook set to ' + hook

        return render_template("simple.html", content = content)
