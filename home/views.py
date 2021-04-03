from django.shortcuts import render,redirect
from django.views.generic import TemplateView
# Create your views here.
from django.conf import settings
import os
class Home(TemplateView):
    template_name = 'index.html'

def add_bot(request):
    token = request.POST.get('token')
    user_id = request.POST.get('user_id')
    bot_path = str(settings.BASE_DIR)+'/home/bot/bot_father.py'
    bot_new = str(settings.BASE_DIR)+'/home/bot/bot_{}.py'.format(user_id)
    bot_conf = str(settings.BASE_DIR)+"/home/conf/bot_conf.conf"
    bot_conf_new = "/etc/supervisor/conf.d/bot_conf_{}.conf".format(user_id)

    with open(bot_path) as f:
        newText = f.read().replace('TOKEN = None', 'TOKEN = "'+token+'"')

    with open(bot_new, "w") as f:
        f.write(newText)

    with open(bot_conf) as f:
        newText = f.read().replace('[program:bot]', '[program:bot_{}]'.format(user_id))
        newText = newText.replace('command=/bot_integrations/venv/bin/python /bot_integrations/home/bot_father.py', 'command=/bot_integrations/venv/bin/python /bot_integrations/home/bot/bot_{}.py'.format(user_id))

    with open(bot_conf_new, "w") as f:
        f.write(newText)

    os.system("supervisorctl reread")
    os.system("supervisorctl update")
    os.system("supervisorctl restart bot_{}".format(user_id))

    return redirect('home')