
cars = [[5,12,1],[16,63,5],[-10,24,2],[7,24,2],[-24,7,2]]
#n = int(input())
#for _ in range(n):
#	cars.append(list(map(int, input().split())))

collide_time = []
for car in cars:
	collide_time.append(exp((car[0]*car[0] +car[1]*car[1]),.5)/(car[2]))
c = 0
collides = 0
sorted(collide_time)
for i in range(len(collide_time)-1):
	if collide_time[i] == collide_time[i+1]:
		c += 1
		collides += c
	else:
		c = 0
print(collides)
