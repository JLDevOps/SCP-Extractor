import re

class SCP:
    def __init__(self, num, wiki):
        self.num = num
        self.wiki = wiki
        if wiki.text:
            self.data = (wiki.text.replace('\n','  ')).replace('\r','  ')
        else:
            self.data = None
    
    def __repr__(self):
        return '''{}
        Title: {}
        Class: {}
        Containment Procedures: {}
        Description: {}
        Addendum: {}
        Document: {}
        Breach Overview: {}
        Link: {}
        '''.format(self.id, self.title, self.object_class,
                    self.containment_procedures, self.description, 
                    self.addendums, self.documents, self.containment_breach_overview, 
                    self.link)
    
    def __iter__(self):
        return iter([
            self.num,
            self.id,
            self.title,
            self.object_class,
            self.containment_procedures,
            self.description,
            self.addendums,
            self.documents,
            self.containment_breach_overview,
            self.link
        ])

    @property
    def id(self):
        return 'SCP-' + str(self.num)
    
    @property
    def link(self):
        return 'http://scp-wiki.net/scp-' + str(self.num)
        
    @property
    def title(self):
        title_re = r': (.*)'
        title_compile = re.compile(title_re)
        try:
            title_group = re.search(title_compile, self.wiki.title)
            return str(title_group.group(1))
        except:
            return None

    @property
    def object_class(self):
        class_re = r'(Object Class: )(.*?)(-|\n| \(| )'
        class_compile = re.compile(class_re)
        try:
            ob_class = re.search(class_compile, self.wiki.text)
            return str(ob_class.group(2))
        except:
            return None
    
    @property
    def containment_procedures(self):
        containment_proc_re = r'(Special Containment Procedures: )(.*?)(«|Description:|Acquisition Log|Containment breach overview: )'
        containment_proc_compile = re.compile(containment_proc_re)
        try:
            procedures = re.search(containment_proc_compile, self.data)
            return str(procedures.group(2))
        except:
            return None

    @property
    def description(self):
        description_re = r'(Description: )(.*?)(«|Acquisition Log|Containment breach|Document(.*)(:)|Addendum(.*)(:))'
        description_compile = re.compile(description_re)
        try:
            description = re.search(description_compile, self.data)
            return str(description.group(2))
        except:
            return None
    
    @property
    def addendums(self):
        addendums_re = r'(Addendum [0-9]{1,3}-[0-9]{1,3}:|Addendum [0-9]{1,3}:|Addendum \d:|Addendum :|Addendum:)(.*?)(«)'
        addendums_compile = re.compile(addendums_re)
        try:
            addendums = re.search(addendums_compile, self.data)
            return str(addendums.group(2))
        except:
            return None
        return None
    
    @property
    def documents(self):
        # TODO Return a list of documents (document number, document info)
        return None
    
    @property
    def containment_breach_overview(self):
        breach_re = r'(Containment breach overview: )(.*?)(«|Document(.*)(:)|Addendum(.*)(:))'
        breach_compile = re.compile(breach_re)
        try:
            breach = re.search(breach_compile, self.data)
            return str(breach.group(2))
        except:
            return None