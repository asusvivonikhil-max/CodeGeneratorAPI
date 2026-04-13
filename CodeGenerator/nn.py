import os
base_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def generate(s,lan):
    if lan=="python":
        if s=="table" or s=="Table":
            with open(r'C:\Users\nikhi\OneDrive\Desktop\Projects\Code Generator\CodeGenerator\CodeGenerator\OuputFiles\Python\Table.txt', 'r+') as file:
               content = file.read()
            return content
        elif s=="sum" or s=="sum"or s=="sub" or s=="Sum"or s=="ADD"or s=="SUM":
            with open(r'C:\Users\nikhi\OneDrive\Desktop\Projects\Code Generator\CodeGenerator\CodeGenerator\OuputFiles\Python\Add.txt', 'r+') as file:
               content = file.read()
            return content
        elif s=="sub" or s=="Sub"or s=="Substraction" or s=="Substract"or s=="diff"or s=="Difference" or s=="DIFF" or s=="difference":
            with open(r'C:\Users\nikhi\OneDrive\Desktop\Projects\Code Generator\CodeGenerator\CodeGenerator\OuputFiles\Python\Sub.txt', 'r+') as file:
               content = file.read()
            return content
        elif s=="mul" or s=="Mul"or s=="Multiplication" or s=="Multiply"or s=="prod"or s=="Product" or s=="PROD" or s=="product":
            with open(r'C:\Users\nikhi\OneDrive\Desktop\Projects\Code Generator\CodeGenerator\CodeGenerator\OuputFiles\Python\Mul.txt', 'r+') as file:
               content = file.read()
            return content
        elif s=="div" or s=="Div"or s=="Division" or s=="Divide"or s=="quot"or s=="Quotient" or s=="QUOT" or s=="quotient":
            with open(r'C:\Users\nikhi\OneDrive\Desktop\Projects\Code Generator\CodeGenerator\CodeGenerator\OuputFiles\Python\Div.txt', 'r+') as file:
               content = file.read()
            return content
        elif s=="table" or s=="Table" or s=="Multiples" or s=="multiples":
            with open(r'C:\Users\nikhi\OneDrive\Desktop\Projects\Code Generator\CodeGenerator\CodeGenerator\OuputFiles\Python\Table.txt', 'r+') as file:
               content = file.read()
            return content
        else:
            return "Sorry, I can't generate code for that query yet."
    elif lan=="java":
        if s=="table" or s=="Table":
            with open(r'C:\Users\nikhi\OneDrive\Desktop\Projects\Code Generator\CodeGenerator\CodeGenerator\OuputFiles\Java\Table.txt', 'r+') as file:
               content = file.read()
            return content
        elif s=="sum" or s=="sum"or s=="sub" or s=="Sum"or s=="ADD"or s=="SUM":
            with open(r'C:\Users\nikhi\OneDrive\Desktop\Projects\Code Generator\CodeGenerator\CodeGenerator\OuputFiles\Java\Add.txt', 'r+') as file:
               content = file.read()
            return content
        elif s=="sub" or s=="Sub"or s=="Substraction" or s=="Substract"or s=="diff"or s=="Difference" or s=="DIFF" or s=="difference":
            with open(r'C:\Users\nikhi\OneDrive\Desktop\Projects\Code Generator\CodeGenerator\CodeGenerator\OuputFiles\Java\Sub.txt', 'r+') as file:
               content = file.read()
            return content
        elif s=="mul" or s=="Mul"or s=="Multiplication" or s=="Multiply"or s=="prod"or s=="Product" or s=="PROD" or s=="product":
            with open(r'C:\Users\nikhi\OneDrive\Desktop\Projects\Code Generator\CodeGenerator\CodeGenerator\OuputFiles\Java\Mul.txt', 'r+') as file:
               content = file.read()
            return content
        elif s=="div" or s=="Div"or s=="Division" or s=="Divide"or s=="quot"or s=="Quotient" or s=="QUOT" or s=="quotient":
            with open(r'C:\Users\nikhi\OneDrive\Desktop\Projects\Code Generator\CodeGenerator\CodeGenerator\OuputFiles\Java\Div.txt', 'r+') as file:
               content = file.read()
            return content
        elif s=="table" or s=="Table" or s=="Multiples" or s=="multiples":
            with open(r'C:\Users\nikhi\OneDrive\Desktop\Projects\Code Generator\CodeGenerator\CodeGenerator\OuputFiles\Java\Table.txt', 'r+') as file:
               content = file.read()
            return content
        else:
            return "Sorry, I can't generate code for that query yet."

    elif lan=="c":
        if s=="table" or s=="Table":
            with open(r'C:\Users\nikhi\OneDrive\Desktop\Projects\Code Generator\CodeGenerator\CodeGenerator\OuputFiles\C\Table.txt', 'r+') as file:
               content = file.read()
            return content
        elif s=="sum" or s=="sum"or s=="sub" or s=="Sum"or s=="ADD"or s=="SUM":
            with open(r'C:\Users\nikhi\OneDrive\Desktop\Projects\Code Generator\CodeGenerator\CodeGenerator\OuputFiles\C\Add.txt', 'r+') as file:
               content = file.read()
            return content
        elif s=="sub" or s=="Sub"or s=="Substraction" or s=="Substract"or s=="diff"or s=="Difference" or s=="DIFF" or s=="difference":
            with open(r'C:\Users\nikhi\OneDrive\Desktop\Projects\Code Generator\CodeGenerator\CodeGenerator\OuputFiles\C\Sub.txt', 'r+') as file:
               content = file.read()
            return content
        elif s=="mul" or s=="Mul"or s=="Multiplication" or s=="Multiply"or s=="prod"or s=="Product" or s=="PROD" or s=="product":
            with open(r'C:\Users\nikhi\OneDrive\Desktop\Projects\Code Generator\CodeGenerator\CodeGenerator\OuputFiles\C\Mul.txt', 'r+') as file:
               content = file.read()
            return content
        elif s=="div" or s=="Div"or s=="Division" or s=="Divide"or s=="quot"or s=="Quotient" or s=="QUOT" or s=="quotient":
            with open(r'C:\Users\nikhi\OneDrive\Desktop\Projects\Code Generator\CodeGenerator\CodeGenerator\OuputFiles\C\Div.txt', 'r+') as file:
               content = file.read()
            return content
        elif s=="table" or s=="Table" or s=="Multiples" or s=="multiples":
            with open(r'C:\Users\nikhi\OneDrive\Desktop\Projects\Code Generator\CodeGenerator\CodeGenerator\OuputFiles\C\Table.txt', 'r+') as file:
               content = file.read()
            return content
        else:
            return "Sorry, I can't generate code for that query yet."
        

    