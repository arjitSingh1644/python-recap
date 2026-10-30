# # # d = {"a":10,"b":60,"c":75,"d":90,"e":80}
# # # largest = 0
# # # second = 0
# # # for key in d:
# # #     value = d[key]
# # #     if largest == 0 or value>largest:
# # #         second = largest


# # #         largest = value
# # #     elif largest>value>second:
# # #         second = value 
# # # print(second) 

# # # # s = "apple orange banana banana banana orange kiwi"
# # # # words=s.split()
# # # # frequency={}
# # # # for word in words:
# # # #     if word in frequency:
# # # #         frequency[word]+=1
# # # #     else:
# # # #         frequency[word]=1
# # # # print(frequency)
# students = {
#     "Aman": {"Math": 80, "English": 65, "Science": 70},
#     "Rohit": {"Math": 35, "English": 75, "Science": 80},
#     "Priya": {"Math": 60, "English": 55, "Science": 45},
#     "Simran": {"Math": 90, "English": 85, "Science": 95}
# }
# result={}
# for name in students:
#     if students[name]["Math"] >= 40 and students[name]["English"] >= 40 and students[name]["Science"] >= 40:
#         result[name]=students[name]
# print(result)
# # # result = {}
# # # for name in students:
# # #     passed = True
# # #     for subject in students[name]:
# # #         if students[name][subject]<40:
# # #             passed = False
# # #             break
# # #     if passed:
# # #         result[name] = students[name]
# # # print(result)

# # # # d = {}
# # # # n = int(input("number of entries"))
# # # # for i in range(n):
# # # #     key =(input("enter key"))
# # # #     value = int(input("enter value"))
# # # #     d[key] = value
# # # # print(d)

# # # d={"a":10,"b":20,"c":10,"d":30,"e":20}
# # # x={}
# # # for i in d:
# # #     if d[i] not in x.values():
# # #         x[i]=d[i]
# # # print(x)
# # d = {}
# # n = int(input("enter how many entries: "))
# # for i in range(n):
# #     key = input("enter key: ")
# #     value = input("enter values" )
# #     d[key] = value
# # print(d)
# s = {1,2,3,4,5,6}
# result = set()

# for i in s:
#     first = i
#     for j in s:
#         second = j
#         if first != second:
#             sum = first + second
#         if sum not in result and sum in s:
#             result.add(sum)

# print(result)
# try:
#     numbers = [10,20,30,40]
#     i = int(input("index: "))
#     print(numbers[i])
# except IndexError:
#     print("index does not exist")
