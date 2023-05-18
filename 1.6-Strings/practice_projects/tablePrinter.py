tableData = [['apples', 'oranges', 'cherries', 'banana'], 
 ['Alice', 'Bob', 'Carol', 'David'], 
 ['dogs', 'cats', 'moose', 'goose']]

def printTable(tableData):
    colWidths = [0] * len(tableData)
    for linha in tableData:
        for i in range(len(linha)-1):
            if len(linha[i]) > colWidths[i]:
                colWidths[i] = len(linha[i])
        
    for linha in tableData:
        output = ''
        for i in range(len(linha)-1):
            output += ' ' + linha[i].rjust(colWidths[i])

        print(output)        

printTable(tableData)
