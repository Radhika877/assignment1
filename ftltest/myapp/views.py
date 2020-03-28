from django.shortcuts import render,redirect
from myapp.forms import PostForm, NewForm
# Create your views here.
from django.http import JsonResponse

def send_json(request):

    data = [{
			"id": "W012A3CDE",
			"real_name": "Egon Spengler",
			"tz": "America/Los_Angeles",
			"activity_periods": [{
					"start_time": "Feb 1 2020  1:33PM",
					"end_time": "Feb 1 2020 1:54PM"
				},
				{
					"start_time": "Mar 1 2020  11:11AM",
					"end_time": "Mar 1 2020 2:00PM"
				},
				{
					"start_time": "Mar 16 2020  5:33PM",
					"end_time": "Mar 16 2020 8:02PM"
				}
			]
		},
		{
			"id": "W07QCRPA4",
			"real_name": "Glinda Southgood",
			"tz": "Asia/Kolkata",
			"activity_periods": [{
					"start_time": "Feb 1 2020  1:33PM",
					"end_time": "Feb 1 2020 1:54PM"
				},
				{
					"start_time": "Mar 1 2020  11:11AM",
					"end_time": "Mar 1 2020 2:00PM"
				},
				{
					"start_time": "Mar 16 2020  5:33PM",
					"end_time": "Mar 16 2020 8:02PM"
				}
			]
		}
	]


    return JsonResponse(data, safe=False)

def index(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
	else:
		form=PostForm()
	return render(request,'home.html',{'form':form})
    
def show(request):
    if request.method == "POST":
        form = NewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form=NewForm()
    return render(request,'showhome.html',{'form':form})