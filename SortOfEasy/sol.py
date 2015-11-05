f = open("sorting-job.in", "r")
nums = f.readline().split(",")
nums[-1] = nums[-1][:-1]
nums = [int(elem) for elem in nums]

f.close()
f = open("sorting-job.out", "w")

nums = reversed(sorted(nums))

f.write(",".join([str(elem) for elem in nums]) + "\n")
f.flush()
