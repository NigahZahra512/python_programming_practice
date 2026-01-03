f = open("demo_2.txt","w")
f.write("this is my new text file")

f = open("demo_2.txt","a")   #:for add new content to old data
f.write("\nWOWWWWWW!")

f.close()