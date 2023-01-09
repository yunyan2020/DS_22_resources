my_list = []

my_list.append("Anton")

my_list.append("Appelblom")

my_list.reverse()

my_list.clear()

my_list.append("Anton")

my_list.append("Appelblom")

count = my_list.count("Korv")
element = my_list.pop()


my_list.append("Appelblom")
my_list.append("Anna")
my_list.append("Alexandersson")

count = my_list.count("Anton")

#Vi kan inte jämföra strängar med siffror så måste vara samma datatyp i listan.
# my_list.append(1)
#my_list.append(True)

my_list.sort(reverse = True)


print(my_list,count,element)

list2 = [1,10,43,4,True,False]
list2.sort()


print(list2)


my_string = "Hej jag heter Anton"
print(my_string)
my_string_list = list(my_string)
print(my_string_list)

my_split_string = my_string.split()
print(my_split_string)

my_split_string = my_string.split('h')
print(my_split_string)

my_split_string = my_string.split('H') #case senstive
print(my_split_string)

my_email ="anton@mujina.se"
my_domain = my_email.split('@')[1].capitalize()
my_domain1 = my_email.split('@')[1].split('.')[0]
print(my_domain)
print(my_domain1)
my_domain = my_email.split('@')[1].upper()
print(my_domain)


split_string = my_email.split('@')
domain = split_string[1]
split_domain = domain.split('.')
print(split_domain)
company = split_domain[0]
print(company)

my_untrimmed_string = "    Anton     "
print(my_untrimmed_string)
my_untrimmed_string = my_untrimmed_string.strip()
print(my_untrimmed_string)

letter_list = ["A","N","T","O","N"]

my_name = "".join(letter_list)
print(my_name)

#funkar inte! Då listor inte har join
#my_name_again = letter_list.join()
#print(my_name_again)
