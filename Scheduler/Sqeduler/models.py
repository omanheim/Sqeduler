from django.db import models

def get_daysint(days):
	st = str(days)
	i = 0
	prod = 1
	while i < len(st):
		x = st[i:i+1]
		if x == 'M': prod = prod * 3
		if x == 'T': prod = prod * 5
		if x == 'W': prod = prod * 7
		if x == 'R': prod = prod * 11 
		if x == 'F': prod = prod * 13
		if x == 'S': prod = prod * 17
		if x == 'U': prod = prod * 19
		i = i + 1
	return prod 

class User(models.Model):
	fname = models.CharField('First name', max_length=20,primary_key=True)
	lname = models.CharField('Last name', max_length=20)
	def __unicode__(self):
		return self.fname	

class Course(models.Model):
	courseid = models.CharField('Course ID',max_length=7)
	section = models.CharField('Section',max_length=3)
	title = models.CharField(max_length=60)
	days = models.CharField(max_length=7)
	daysint = models.IntegerField(blank=True, editable=False)
	starttime = models.TimeField('Start time')
	endtime = models.TimeField('End time')
	def __unicode__(self):
		return self.courseid
	def save(self):
		self.daysint = get_daysint(self.days)
		super(Course, self).save()

class Enrollment(models.Model):
	fname = models.ForeignKey(User, verbose_name="first name")
	courseid = models.ForeignKey(Course, verbose_name="course")
	def __unicode__(self):
		return u'%s in %s' % (self.fname, self.courseid)
