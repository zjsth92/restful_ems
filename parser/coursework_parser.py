from lxml import html

COURSE_WORK_TABLE = "//tr"
TYPE_XPATH = COURSE_WORK_TABLE + "/td[1]/a"
TITLE_XPATH = COURSE_WORK_TABLE + "/td[2]/a"
LINK_XPATH = COURSE_WORK_TABLE + "/td[2]/a/@href"
POINTS_XPATH = COURSE_WORK_TABLE + "/td[3]"
AVAILABLE_XPATH = COURSE_WORK_TABLE + "/td[4]"
DUE_XPATH = COURSE_WORK_TABLE + "/td[5]"
SUBMITTED_XPATH = COURSE_WORK_TABLE + "/td[7]"

def parse(text):
    tree = html.fromstring(text)

    types = tree.xpath(TYPE_XPATH)
    titles = tree.xpath(TITLE_XPATH)
    points = tree.xpath(POINTS_XPATH)
    availables = tree.xpath(AVAILABLE_XPATH)
    dues = tree.xpath(DUE_XPATH)
    submits = tree.xpath(SUBMITTED_XPATH)
    links = tree.xpath(LINK_XPATH)

    course_works = []

    for i in range(0, len(points)):
        due = dues[i].text
        if due is not None:
            course_works.append({
                "type": types[i].text,
                "title": titles[i].text,
                "link": links[i],
                "point": points[i].text,
                "available": availables[i].text,
                "due": dues[i].text,
                "submit": "" if submits[i].text is None else submits[i].text.replace("\n", "")
            })
            
    return course_works