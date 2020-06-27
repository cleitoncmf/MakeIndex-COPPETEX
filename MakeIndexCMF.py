import sys
import os



# Function for reading a file line by line
def ReadLines(filename):
    lines = []
    with open(filename) as fp:
        line = fp.readline()
        while line:
            lines.append(line)
            line = fp.readline()
    return lines



# Function to extrac:
# - The label
# - The definition
# - The page
def ExtractInfo(string):
    aux1 = string.split('[')
    aux2 = aux1[1].split('] ')
    label = aux2[0]

    aux3 = aux2[1].split('|')
    definition = aux3[0]

    aux4 = aux3[1].split('{')
    aux5 = aux4[1].split('}')
    pg = aux5[0]
    
    return label,definition,pg


# Function to write the '.los' file
def Writelosfile(name,InfoLines):
    file = open(name, 'w+')
    file.write('\\begin{theglossary}\n')
    file.write('\\makeatletter\n')
    file.write('\\setlength{\\labelwidth}{2.0cm}\n')
    file.write('\\setlength{\\itemindent}{0.0cm}\n')

    for item in InfoLines:
        label,definition,pg = ExtractInfo(item)
        string = '\item [' + label + '] ' + definition + ', p. \hyperpage{' + pg + '}\n'
        file.write(string)        
        
    
    file.write('\\end{theglossary}\n')

   
    file.close()


# Testes
L = ReadLines('main.syx')
Writelosfile('main.los',L)
#T,Q,U = ExtractInfo(L[100])


