rows = [[1]]
rows.append([1,1])
n = int(input("enter the nbr of the row u want to see: "))
def pascal_triangle(n):
    for i in range(2,n+1):
      row = []
      row.append(1)
      for j in range(1,i):
        row.append(rows[i-1][j]+rows[i-1][j-1])
      row.append(1)
      rows.append(row)
    return rows[n-1]

print(pascal_triangle(n))