n = int(input())
arr = input().split()
runnerUp=-100
champion=-100

for i in range(0,n):
	if int(arr[i]) > int(champion):
		runnerUp= champion
		champion= arr[i]
	if int(arr[i]) > int(runnerUp) and int(arr[i]) < int(champion):
		runnerUp = arr[i]
print(runnerUp)

