files = ["a_example", "b_small", "c_medium", "d_quite_big", "e_also_big"]

user = int(input("input 1-5 (in order of smallest file to biggest): "))
file = open(files[user - 1] + ".in", "r").read().strip().split("\n")

maximum = int(file[0].split(" ")[0])
constantSlices = [int(i) for i in file[1].split(" ")]
slices = [int(i) for i in file[1].split(" ")]

result = []
final = []
while sum(slices) > maximum:
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

output.write(str(len(final[finalSums.index(max(finalSums))])) + "\n")

finalTuple = final[finalSums.index(max(finalSums))]
finalTuple.sort()

line2 = ""
for i in finalTuple:
	line2 += str(constantSlices.index(i)) + " "
output.write(line2 + "\n")