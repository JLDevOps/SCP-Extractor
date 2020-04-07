import re

# Following template format
# **Item #:** SCP-XXXX
# **Object Class:** Safe/Euclid/Keter (indicate which class)
# **Special Containment Procedures:** [Paragraphs explaining the procedures]
# **Description:** [Paragraphs explaining the description]
# **Addendum:** [Optional additional paragraphs]
# ** Document**

class SCP:
    def __init__(self, num, wiki):
        self.num = num
        self.wiki = wiki
    
    @property
    def item_num(self):
        return 'SCP-' + str(self.num)
    
    @property
    def link(self):
        return 'http://scp-wiki.net/scp-' + str(self.num)
        
    @property
    def title(self):
        title_re = r': (.*)'
        title_compile = re.compile(title_re)
        title_group = re.search(title_compile, self.wiki.title)
        return str(title_group.group(1))

    @property
    def object_class(self):
        class_re = r'(Object Class: )(.*\n)'
        class_compile = re.compile(class_re)
        ob_class = re.search(class_compile, self.wiki.text)
        try:
            return str(ob_class.group(2)).replace('\n', '')
        except:
            return None
    
    @property
    def containment_procedures(self):
        data = self.wiki.text.replace('\n','  ')
        data = data.replace('\r','  ')

        containment_proc_re = r'Special Containment Procedures:'
        containment_proc_re_description = r'(Special Containment Procedures: )(.*?)(  Description: |«)'

        containment_proc_regex = re.compile(containment_proc_re)
        description_regex = re.compile(description_re_no_filter)
        containment_proc_desc_compile = re.compile(containment_proc_re_description)

        if (containment_proc_regex.search(data)):
            procedures = re.search(containment_proc_desc_compile, data)
            return str(procedures.group(2))
        else:
            return None

    @property
    def description(self):
        data = self.wiki.text.replace('\n','  ')
        data = data.replace('\r','  ')

        description_re_search = r'Description:'
        description_re_ad = r'(Description: )(.*?)(Addendum)(.*)(:)'
        description_re_doc = r'(Description: )(.*?)(Document)(.*)(:)'
        description_re_no_filter = r'(Description: )(.*?)(«)'
        addendum_re = r'(Addendum)(.*)(:)'
        document_re = r'(Document)(.*)(:)'

        description_search_compile = re.compile(description_re_search)
        description_ad_compile = re.compile(description_re_ad)
        description_doc_compile = re.compile(description_re_doc)
        description_re_no_filter_compile = re.compile(description_re_no_filter)
        addendum_compile = re.compile(addendum_re)
        document_compile = re.compile(document_re)

        if (description_search_compile.search(data)):
            if(addendum_compile.search(data)):
                description = re.search(description_ad_compile, data)
                return str(description.group(2))
            elif (document_compile.search(data)):
                description = re.search(description_doc_compile,data)
                return str(description.group(2))
            else:
                description = re.search(description_re_no_filter_compile,data)
                return str(description.group(2))
        else:
            return None

    

