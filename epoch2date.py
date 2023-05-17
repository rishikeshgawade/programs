import sys
import datetime as dt
input_file=sys.argv[1]
fp=open(input_file,"r")
for line in fp.readlines():
	edate,*msg=line.split(":")
	date=dt.datetime.fromtimestamp(float(edate))
	datetime = date.strftime("%a %d %b %T.%s %Z %Y")
	if(len(msg)>=2):
		print(str(datetime)+":"+msg[0]+":"+msg[2],end="")
	else:
		print(str(datetime)+":"+msg[0],end="")
