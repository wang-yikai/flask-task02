#Yikai Wang
#Period 6 SoftDev

from flask import Flask, render_template
app = Flask(__name__) #create Flask object

def importCSV(fileName):
    inStream = open(fileName, 'r')
    lines = inStream.readlines()
    inStream.close()
    return lines

def cleanUp(L):
    for w in range(len(L)):
        L[w] = L[w].strip()
        L[w] = L[w].strip( "\n" )
        L[w] = L[w].strip( "\r" )
        if ('"' in L[w][0]):
            L[w] = L[w].split( '"' )[1:]
            L[w][1] = L[w][1][1:]
        else:
            L[w] = L[w].split( ',' )
    return L

def convertToDictionary(fileName):
    L = cleanUp(importCSV(fileName))
    #print L
    D = dict()
    for subL in L:
        #print subL
        #print ""
        D[subL[0]] = subL[1]
    return D

@app.route("/occupations")
D = convertToDictionary("occupations.csv")

def makeHTML():
    return render_template( 'template.html', title="Occupations List", collection = D )

@app.route("/") #assign following fxn to run when root route requested
def intro():
    return "Hello, there is nothing here!"

if __name__ == "__main__":
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()