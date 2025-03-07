names=['bhavani','salaar','varadha']
nums=[9.5,'bhavani',25]
combi=[names,nums]
print(combi)
nums.append(45) #append add the thing in () at the last
print(nums)
nums.remove(25) #it removes
print(nums)
nums.pop(1) # pops out the given position
print(nums)
nums.extend([1,2,3,4,5]) #extends and adds it
print(nums)
del nums[4:] #deletes the values
print(nums)
print(min(nums)) #min value
print(max(nums)) #max value
print(sum(nums)) # sum
nums.sort() #used for sortin i.e ascending order
print(nums)