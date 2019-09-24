
#al
offsets = [131.7,4628.400000000001,6976.0,15684.6,22526.300000000003,26028.3]
filename = "al-timed"
output = open('al-complete.txt','w')

for i in range(1,7):
	filename = "al-timed" + str(i) + ".txt"
	lines = open(filename,'r').readlines()
	for line in lines:
		newline = line
		if len(newline.split())!=0:
			time = line.split()[0]
			newtime = str(float(time) + offsets[i-1])
			newline = newtime + newline[len(time):]
		output.write(newline)

output.close()


#betrand
offsets = [13.4,9745.4,19477.4]
output = open('betrand-complete.txt','w')

for i in range(1,4):
	filename = "betrand-timed" + str(i) + ".txt"
	lines = open(filename,'r').readlines()
	for line in lines:
		newline = line
		if len(newline.split())!=0:
			time = line.split()[0]
			newtime = str(float(time) + offsets[i-1])
			newline = newtime + newline[len(time):]
		output.write(newline)

output.close()

#caitlin
offsets = [15467.400000000001,22496.4]

output = open('caitlin-complete.txt','w')

for i in range(1,3):
	filename = "caitlin-timed" + str(i) + ".txt"
	lines = open(filename,'r').readlines()
	for line in lines:
		newline = line
		if len(newline.split())!=0:
			time = line.split()[0]
			newtime = str(float(time) + offsets[i-1])
			newline = newtime + newline[len(time):]
		output.write(newline)

output.close()

#ingrid
offsets = [18706.1]
output = open('ingrid-complete.txt','w')

for i in range(1,2):
	filename = "ingrid-timed" + str(i) + ".txt"
	lines = open(filename,'r').readlines()
	for line in lines:
		newline = line
		if len(newline.split())!=0:
			time = line.split()[0]
			newtime = str(float(time) + offsets[i-1])
			newline = newtime + newline[len(time):]
		output.write(newline)

output.close()


#lin
offsets=[115.1]
output = open('lin-complete.txt','w')

for i in range(1,2):
	filename = "lin-timed" + str(i) + ".txt"
	lines = open(filename,'r').readlines()
	for line in lines:
		newline = line
		if len(newline.split())!=0:
			time = line.split()[0]
			newtime = str(float(time) + offsets[i-1])
			newline = newtime + newline[len(time):]
		output.write(newline)
output.close()
#matthew
offsets=[0.4,6262.4]
output = open('matthew-complete.txt','w')

for i in range(1,3):
	filename = "matthew-timed" + str(i) + ".txt"
	lines = open(filename,'r').readlines()
	for line in lines:
		newline = line
		if len(newline.split())!=0:
			time = line.split()[0]
			newtime = str(float(time) + offsets[i-1])
			newline = newtime + newline[len(time):]
		output.write(newline)

output.close()
#paulo
offsets = [161.2,19193.0]

output = open('paulo-complete.txt','w')

for i in range(1,3):
	filename = "paulo-timed" + str(i) + ".txt"
	lines = open(filename,'r').readlines()
	for line in lines:
		newline = line
		if len(newline.split())!=0:
			time = line.split()[0]
			newtime = str(float(time) + offsets[i-1])
			newline = newtime + newline[len(time):]
		output.write(newline)
output.close()
#peter
offsets=[0,7136.4]
output = open('peter-complete.txt','w')

for i in range(1,3):
	filename = "peter-timed" + str(i) + ".txt"
	lines = open(filename,'r').readlines()
	for line in lines:
		newline = line
		if len(newline.split())!=0:
			time = line.split()[0]
			newtime = str(float(time) + offsets[i-1])
			newline = newtime + newline[len(time):]
		output.write(newline)
output.close()

#win
offsets = [1.7]
output = open('win-complete.txt','w')

for i in range(1,2):
	filename = "win-timed" + str(i) + ".txt"
	lines = open(filename,'r').readlines()
	for line in lines:
		newline = line
		if len(newline.split())!=0:
			time = line.split()[0]
			newtime = str(float(time) + offsets[i-1])
			newline = newtime + newline[len(time):]
		output.write(newline)

output.close()

#xavier
offsets=[1622.5,11329.5,21036.5]

output = open('xavier-complete.txt','w')

for i in range(1,4):
	filename = "xavier-timed" + str(i) + ".txt"
	lines = open(filename,'r').readlines()
	for line in lines:
		newline = line
		if len(newline.split())!=0:
			time = line.split()[0]
			newtime = str(float(time) + offsets[i-1])
			newline = newtime + newline[len(time):]
		output.write(newline)
output.close()


#yj
offsets = [4.6,4623.9,11206.1,15944.2,27684.9]

output = open('yj-complete.txt','w')

for i in range(1,6):
	filename = "yj-timed" + str(i) + ".txt"
	lines = open(filename,'r').readlines()
	for line in lines:
		newline = line
		if len(newline.split())!=0:
			time = line.split()[0]
			newtime = str(float(time) + offsets[i-1])
			newline = newtime + newline[len(time):]
		output.write(newline)

output.close()

#yoav

offsets = [1,15553.5]

output = open('yoav-complete.txt','w')

for i in range(1,3):
	filename = "yoav-timed" + str(i) + ".txt"
	lines = open(filename,'r').readlines()
	for line in lines:
		newline = line
		if len(newline.split())!=0:
			time = line.split()[0]
			newtime = str(float(time) + offsets[i-1])
			newline = newtime + newline[len(time):]
		output.write(newline)

output.close()




