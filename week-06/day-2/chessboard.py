def chessboard(s):
    rows_and_columns = s.split(' ')
    chars = ['*', '.']
    rows = ''
    if int(rows_and_columns[0]) > 0 and int(rows_and_columns[1]) > 0:
        for i in range(int(rows_and_columns[0])):
            row = ""
            for j in range(int(rows_and_columns[1])):
                row += (chars[(i+j)%2])
            rows += row 
            if i < int(rows_and_columns[0])-1:
                rows += "\n"
        return rows
    else:
        return ''

print (chessboard("2 2"))