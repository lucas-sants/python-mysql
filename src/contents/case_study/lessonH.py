enter = open("18s_humano.fasta").read()
exit = open("18s_humano.html", "w")

cont = {}

for i in ['A', 'T', 'C', 'G']:
	for j in ['A', 'T', 'C', 'G']:
		cont[i+j] = 0

enter = enter.replace("\n","")

for k in range(len(enter)-1):
	cont[enter[k]+enter[k+1]] += 1

print(cont)

# HTML

i = 1
for k in cont:
	transparency = cont[k]/max(cont.values())
	exit.write("<div style='width:100px, border:1px solid #111; height:100px; float:left; background-color:rgba(0, 0, 255, "+str(transparency)+"')></div>")

	if i%4 == 0:
		exit.write("<div style='clear:both'></div>")

	i+=1

exit.close()