from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.http import Http404
import datetime

from Sqeduler.models import User, Course, Enrollment

def convert_day(day):
	if (day == 0): return 3
	if (day == 1): return 5
	if (day == 2): return 7
	if (day == 3): return 11
	if (day == 4): return 13
	if (day == 5): return 17
	if (day == 6): return 19

def write_out_day(day):
	if (day == 0): return "Monday" 
	if (day == 1): return "Tuesday"
	if (day == 2): return "Wednesday" 
	if (day == 3): return "Thursday"
	if (day == 4): return "Friday"
	if (day == 5): return "Saturday"
	if (day == 6): return "Sunday"

def number_of_day(day):
	if (day == "Monday" or day == "monday"): return 0
	if (day == "Tuesday" or day == "tuesday"): return 1
	if (day == "Wednesday" or day == "wednesday"): return 2
	if (day == "Thursday" or day == "thursday"): return 3
	if (day == "Friday" or day == "friday"): return 4
	if (day == "Saturday" or day == "saturday"): return 5
	if (day == "Sunday" or day == "sunday"): return 6
	
def index(request):
	courselist = Course.objects.order_by('title')
	context = {'courselist': courselist}
	return render(request, 'Sqeduler/index.html', context)

def dayschedule(request, day):
	nday = number_of_day(day) 
	fullday = write_out_day(nday)
	nday = convert_day(nday)
	courselist = Course.objects.order_by('days','starttime')
	dict = {'day':nday, 'courselist': courselist, 'fullday': fullday}
	return render(request, 'Sqeduler/givenday.html', dict)

def detail(request, course_id, id):
	course = get_object_or_404(Course, pk=id)
	dict = {'c_id': course.courseid, 'c_title': course.title, 'c_days': course.days, 'c_stime': course.starttime, 'c_etime': course.endtime}
	return render(request, 'Sqeduler/detail.html', dict) 

def today(request):
	day = datetime.datetime.today().weekday()
	fullday = write_out_day(day)
	day = convert_day(day)
	courselist = Course.objects.order_by('days','starttime')
	dict = {'day':day, 'courselist': courselist, 'fullday': fullday}
	return render(request, 'Sqeduler/today.html', dict)

def now(request):
	time = datetime.datetime.today().time()
	courselist = Course.objects.order_by('days','starttime')
	dict = {'courselist': courselist, 'time': time}
	return render(request, 'Sqeduler/now.html', dict)

def whoswhere(request):
	time = datetime.datetime.today().time()
	day = datetime.datetime.today().weekday()
	fullday = write_out_day(day)
	day = convert_day(day)
	courselist = Course.objects.order_by('days','starttime')
	userlist = User.objects.order_by('fname','lastname')	
	enrollmentlist = Enrollment.objects.order_by('fname')
	dict = {'courselist':courselist,'time':time,'day':day,'fullday':fullday,'enrollmentlist': enrollmentlist}
	return render(request, 'Sqeduler/whoswhere.html', dict)		
