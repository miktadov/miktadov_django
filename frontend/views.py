from django.shortcuts import render, redirect
from django.contrib import messages
# from django_user_agents.utils import get_user_agent
from .models import MyForm


def start(request):
	# user_agent = get_user_agent(request)
	if request.user_agent.is_mobile or request.user_agent.is_tablet or request.user_agent.is_touch_capable:
		messages.success(request, 'mobile')
		return render(request, "index_mobile.html")
	else:
		messages.success(request, 'pc')
		return render(request, "index.html")


def send_form(request):
	if request.method == 'POST':
		form = MyForm(colled=False)
		form.name = request.POST['user_name']
		form.comm = request.POST['user_contact']
		form.mess = request.POST['user_message']
		form.save()
		messages.success(request, f'{form.name}, thank you for leaving a request. In the near future I will contact you using your contacts: {form.comm}')
		return redirect('start')
	else:
		messages.success(request, 'Ошибка формы!')
		return redirect('start')
