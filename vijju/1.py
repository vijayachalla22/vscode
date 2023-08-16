import re
story ="my name is vijaya, and i work in hallmark at kakinada is city in andhra pradesh"
m= {
    "name" : "vijaya",
    "company" : "hallmark",
    "city" : "kakinada",
    "favorite" : "kaja"

}
final_list = []
search_list = m.values()

for x in search_list:
    for y in re.finditer(x,story):
        start_index = story.find(x)
        end_index = start_index + (len(x)-1)
        list = [x,start_index,end_index]
        final_list.append(list)
print(final_list)