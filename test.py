n=int(input())
mat=[]
for _ in range(n):
    mat.append(list(input()))
print(mat)


n = int(input("Enter the size of the list "))
print("\n")
num_list = list(int(num) for num in input("Enter the list items separated by space ").strip().split())[:n]

print("User list: ", num_list)