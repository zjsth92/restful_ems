from lxml import html

USER_NAME_XPATH = "/html[@class='no-js']/body[@id='dashboard-show']/header/div[@class='col-xs-12']/nav[@class='secondary']/ul[@class='nav nav-pills']/li[@class='mini-profile pull-right'][1]/text()"

TRIMESTER_XPATH = "//div[@class='course_list_cell component full-width']/heading/h4/div/a/text()"

COURSES_TABLE_XPATH = "/html/body//div[@class='course_list_cell component full-width']/table/tbody/tr"
COURSE_CODE_XPATH = COURSES_TABLE_XPATH +  "/td[1]/text()"
SECTION_CODE_XPATH = COURSES_TABLE_XPATH + "/td[2]/text()"
COURSE_NAME_XPATH = COURSES_TABLE_XPATH + "/td[3]/a/text()"
COURSE_LINK_XPATH = COURSES_TABLE_XPATH +  "/td[3]/a/@href"
COURSE_CREDIT_XPATH = COURSES_TABLE_XPATH + "/td[4]/text()"
COURSE_GRADE_XPATH = COURSES_TABLE_XPATH + "/td[6]/text()"


def parse(text):
    tree = html.fromstring(text)
    # username = getUsername(tree)
    courses = getCourses(tree)
    trimester = tree.xpath(TRIMESTER_XPATH)[0].lower().replace(" ", "_")
    return {
        # "username": username,
        "courses": courses,
        "trimester": trimester
    }
    

def getUsername(tree):
    username = tree.xpath(USER_NAME_XPATH)
    return username[0].replace("\n", "")

def getCourses(tree):
   
    course_codes = tree.xpath(COURSE_CODE_XPATH)
    section_codes = tree.xpath(SECTION_CODE_XPATH)
    course_names = tree.xpath(COURSE_NAME_XPATH)
    course_links = tree.xpath(COURSE_LINK_XPATH)
    course_credits = tree.xpath(COURSE_CREDIT_XPATH)
    course_grades = tree.xpath(COURSE_GRADE_XPATH)

    courses = []

    for i in range(0, len(course_codes)-1):
        courses.append({
            "code": course_codes[i],
            "section": section_codes[i],
            "name": course_names[i],
            "link": course_links[i],
            "credit": course_credits[i],
            "grade": course_grades[i]
        })

    return courses