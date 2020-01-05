files = ["a_example", "b_small", "c_medium", "d_quite_big", "e_also_big"]

user = int(input("input 1-5 (in order of smallest file to biggest): "))
file = open(files[user - 1] + ".in", "r").read().strip().split("\n")

maximum = int(file[0].split(" ")[0])
pizzas = [int(i) for i in file[1].split(" ")]

constantSlices = list(dict.fromkeys(pizzas))
slices = list(dict.fromkeys(pizzas))

result = []
final = []
while sum(slices) > maximum * .75:
	for i in range(1, len(slices) + 1):
		index = -i
		if sum(result) + slices[index] <= maximum:
			result.append(slices[index])
		else:
			continue
	final.append(result)
	result = []
	del slices[-1]


output = open("answers/" + files[user - 1] + "_answer.txt", "w")

finalSums = [sum(i) for i in final]
print("MAX:", max(finalSums))

output.write(str(len(final[finalSums.index(max(finalSums))])) + "\n")

finalTuple = final[finalSums.index(max(finalSums))]
finalTuple.sort()

line2 = ""
for i in finalTuple:
	line2 += str(constantSlices.index(i)) + " "
output.write(line2 + "\n")