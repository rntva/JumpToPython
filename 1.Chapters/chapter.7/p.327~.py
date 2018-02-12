from xml.etree.ElementTree import Element, dump, SubElement, ElementTree, parse

# note = Element("note")
# to = Element("to")
# to.text = "Tove"
#
# note.append(to)
# dump(note)

note = Element("note") # same as note = Element("note", date = "20180108")
note.attrib["date"] = "20180108"
note.attrib["editor"] = "Pycharm"


to = Element("to")
to.text = "Tove"
note.append(to)

SubElement(note, "from").text = "Jani"
SubElement(note, "heading").text = "Reminder"
SubElement(note, "body").text = "Don't forget me this weekend!"
SubElement(note, "temp").text = "김상엽"
SubElement(note, "temp").text = "김인한"
SubElement(note, "temp").text = "김기정"

# dump(note)

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

indent(note)
dump(note)
ElementTree(note).write("note.xml")

tree = parse("note.xml")
note = tree.getroot()
to_tag = note.find("to")
from_tag = note.find("from")
from_text = note.findtext("from")
from_tags = note.findall("from")
heading_tag = note.find("heading")
body_tag = note.find("body")

from_ttag = note.find("temp")
from_ttext = note.findtext("temp")
from_ttags = note.findall("temp")

# print(note.get("date"))
# print(note.get("money", "default"))
# print(note.items())
# print(to_tag)
# print(from_tag)
# print(from_tag)
# print(from_tags)
# print(from_text)
# print(heading_tag)
# print(body_tag)
# print(from_ttag)
# print(from_ttags)
# print(from_ttext)
# print(from_ttags[0].text)

# for x in from_ttags :
#     print(x.text)

# from_tag = note.findall("from")
# print(from_tag.items())

# print(dir(from_tag))

# temp = note.getchildren()

print("Search from root")
for parent in note.getiterator() :
    for child in parent :
        print(child.text)

# note = tree.getroot()
print("Search from heading")
for child in note.getiterator("heading") :
    print(child.text)

print("end")
