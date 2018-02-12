from xml.etree.ElementTree import Element, SubElement, ElementTree, dump, parse

blog = Element("blog", date = "20180108", editor = "Pycharm")
SubElement(blog, "subject").text = "Why Python"
SubElement(blog, "author").text = "Eric\n  "
SubElement(blog[1], "age").text = "58"
SubElement(blog[1], "natin").text = "USA"
# author = Element("author")
# author.text = "Eric"
# SubElement(author, "age").text = "58"
# SubElement(author, "natin").text = "USA"
# blog.append(author)
SubElement(blog, "Agenda")
SubElement(blog[2], "a").text = "Data Type"
SubElement(blog[2], "b").text = "Controll Flow"
SubElement(blog[2], "c").text = "Function"
# Agenga = Element("Agenda")
# SubElement(Agenga, "a").text = "Data Type"
# SubElement(Agenga, "b").text = "Controll Flow"
# SubElement(Agenga, "c").text = "Function"
# blog.append(Agenga)

# age = Element("age")
# age.text = "58"
# blog.

def indent(elem, level = 0) :
    i = "\n" + level * " "
    if len(elem) :
        if not elem.text or not elem.text.strip() :
            elem.text = i + " "
        if not elem.tail or not elem.tail.strip() :
            elem.tail = i
        for elem in elem :
            indent(elem, level + 1)
        if not elem.tail or elem.tail.strip() :
            elem.tail = i

    else :
        if level and (not elem.tail or not elem.tail.strip()) :
            elem.tail = i

print("bolg의 속성 : " + str(blog.keys()))
indent(blog)
print("\nblog 전체 출력")
dump(blog)
ElementTree(blog).write("blog.xml")

tree = parse("blog.xml")
blog = tree.getroot()

print("\nsubject_text = blog.findtext(\"subject\")")
subject_text = blog.findtext("subject")
print(subject_text)

print("\nsubject_tags = blog.findall(\"author\")")
subject_tags = blog.findall("author")
for x in subject_tags :
    for y in x :
        print(y.tag + " : " + y.text)

print("\nblog.getiterator(\"Agenda\")")
for x in blog.getiterator("Agenda") :
    for y in x:
        print(y.tag + " : " + y.text)




