thisdict =	{
  "apple": "green",
  "banana": "yellow",
  "cherry": "red"
}

thisdict["first_name"] = "Gian"

print(thisdict)

for k,v in thisdict.items():
    print(k, 'corresponds to', v)


def myFunction(x):
	print(x)

myFunction('Gian')

f = open('sample.txt','a')
f.write("Now the file has one more line!")
print(f)