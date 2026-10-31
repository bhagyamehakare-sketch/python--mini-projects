questions=[
    ["who is sha rukh khan?","WWE WRESTLER","ACTOR","ASTRONAUT","PLUMBER",2],
    ["What is the capital of France?","Rome","paris","london","Berlin",3],
    ["which planet is know as a red planet?","Earth","mars","venus","jupiter",2],
    ["what is the largest mamal","elephant","blue whale","giraffe","shark",2],
    ["who wrote 'Remeo and juliet'?","charles Dickens","william shakespeare","jane Austen","homer",2],
    ["what is the square root of 62?","6","8","10","12",4],
    ["which country is known as the land of the rising sun?","china","japan","south korea","india",3],
    ["who painted the mona lisa?","vincent van gogh","pablo picasso","leonardo da vinci","claude monet",3]
]
prizes=[1000,2000,3000,4000,5000,6000,7000,8000]
i=0
for question in questions:
 
    print(question[0])
    print(f"a.{question[1]}")
    print(f"b.{question[2]}")
    print(f"c.{question[3]}")
    print(f"d.{question[4]}")
    #check whther the ans is correct or not
    a=int(input("enter youre ans.1 for a/, 2 for b/, 3 for c/, 4 for d"))
    if(question[5]==a):
        print("correct answer")
    else:
        print(f"incoorect ans the correct ans was,{question[5]} ")
        print("better of next time!")
        break
    print(f"you won {prizes[i]}")
    i += 1
