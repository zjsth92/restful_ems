from lxml import html

TASK_NAME_XPATH = "//div[@class='panel-body']/h4[1]/text()"

TASK_DESC_XPATH = "//div[@class='user-content']//text()"

DOCUMENTS_XPAH = "//table[@class='table table-hover table-bordered'][1]//tr"
DOCUMENT_NAME_XPATH = DOCUMENTS_XPAH + "/td[1]/text()"
DOCUMENT_SIZE_XPATH = DOCUMENTS_XPAH + "/td[2]/text()"
DOCUMENT_LINK_XPATH = DOCUMENTS_XPAH + "/td[3]/a/@href"


def parse(text):
    tree = html.fromstring(text)

    title = tree.xpath(TASK_NAME_XPATH)
    if len(title) > 0:
        title = "".join(title).replace('\n', '')

    desc = tree.xpath(TASK_DESC_XPATH)

    document_names = tree.xpath(DOCUMENT_NAME_XPATH)

    document_sizes = tree.xpath(DOCUMENT_SIZE_XPATH)
    document_links = tree.xpath(DOCUMENT_LINK_XPATH)

    documents = []

    for i in range(0, len(document_names)):
        documents.append({
            "name": document_names[i],
            "link": document_links[i],
            "size": document_sizes[i]
        })

    return {
        "title": title,
        "desc": desc,
        "documents": documents
    }