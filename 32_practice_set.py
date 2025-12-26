# with open("poem.txt") as f:
#     content=f.read()
#     if "Twinkle" in content:
#         print("Twinkle is present in poem")
#     else:
#         print("Twinkle is not present in poem")

# import random
# def game():
#     print("you are playing the game")
#     currentscore=random.randint(1,62)
#     with open("Hi-score.txt") as f:
#         score=f.read()
#         if(score!=""):
#             highscore=int(score)
#         else:
#             highscore=0
#     print(f"your score: {currentscore}")
#     if(currentscore>highscore):
#         with open("Hi-score.txt","w") as f:
#             f.write(str(currentscore))

#         return currentscore
# game()

# def generatetable(n):
#     table=""
#     for i in range(1,11):
#         table += f"{n} x {i} = {n*i}\n"

#     with open(f"table/table{n}.txt","w") as f:
#          f.write(table)

# for i in range(2,21):
#     generatetable(i)

# word="donkey"
# with open("file.txt","r") as f:
#     content=f.read()
# content=content.replace(word,"######")
# with open("file.txt","w") as f:
#     f.write(content)

# l=["nice","bad"]
# with open("file.txt","r") as f:
#     content=f.read()
# for word in l:
#  content=content.replace(word , "#####")
# with open("file.txt","w") as f:
#     f.write(content)

# word="python"
# with open("file.txt" ,"r") as f:
#     content=f.read()
#     if word in content:
#         print("python is present")
#     else:
#         print("python is not present")


# with open("file.txt","r") as f:
#     lines=f.readlines()
# lineno=1
# for line in lines:
#     if "python" in line:
#         print(f"python is present in line at {lineno}")
#         break
#     lineno+=1
# else:
#         print("python is not present in file")

# with open("file.txt","r") as f:
#     content_1=f.read()

# with open("copy_file.txt","w") as f:
#     content_2=f.write(content_1)

# with open("file.txt","r") as f:
#     content_1=f.read()
# with open ("copy_file.txt","r") as f:
#     content_2=f.read()
# if(content_1==content_2):
#     print("Content in both file is same: ")
# else:
#     print("content is not same in both file")

# with open("file.txt","w") as f:
#  f.write("")

# with open("file.txt","r") as f:
#     content=f.read()

# with open("renamed_by_python.txt","w") as f:
#     f.write(content)
