import pyscp
import re
import scp

title_re = r': (.*)' # Capture Group 1
class_re = r'(Object Class: )(.*\n)' # Capture Group 1
containment_procedures_re = r'(Special Containment Procedures: )(.*)(«)'

def extract_title(data=None):
    title_group = re.search(': (.*)', data)
    return str(title_group.group(1))

def extract_object_class(data=None):
    ob_class = re.search(class_re, data)
    return str(ob_class.group(2)).replace('\n', '')

def extract_containment_procedures(data=None):
    data = data.replace('\n', '')
    data = data.replace('\r', '')

    containment_proc_re = r'Special Containment Procedures: '
    containment_proc_re_description = r'(Special Containment Procedures: )(.*)(Description:)'
    containment_proc_re_no_description = r'(Special Containment Procedures: )(.*)(«)'

    containment_proc_regex = re.compile(containment_proc_re)
    
    description_re_no_filter = r'Description:'
    description_re_ad = r'(Description: )(.*)(Addendum)(.*)(:)'
    description_re_doc = r'(Description: )(.*)(Document)(.*)(:)'
    addendum_re = r'(Addendum)(.*)(:)'
    document_re = r'(Document)(.*)(:)'
    

    description_regex = re.compile(description_re_no_filter)
    addendum_regex = re.compile(addendum_re)
    document_regex = re.compile(document_re)


    if (containment_proc_regex.search(data)):
        if(description_regex.search(data)):
            procedures = re.search(containment_proc_re_description, data)
            return str(procedures.group(2))
        else:
            procedures = re.search(containment_proc_re_no_description, data)
            return str(procedures.group(1))
    else:
        return None

    # if(addendum_regex.search(data)):
    #     print('found addendum')
    #     procedures = re.search(description_re_ad, data)
    #     return str(procedures.group(2))
    # elif (document_regex.search(data)):
    #     print('found document')
    #     procedures = re.search(description_re_doc, data)
    #     return str(procedures.group(2))
    # else:
    #     print('found no filter')
    #     procedures = re.search(description_re_no_filter, data)
    #     return str(procedures.group(2))

def extract_description(data=None):
    return None

def download_snapshot(wiki_url=None, db_path=None, forums=False, new_run=False):
    try:
        wiki = pyscp.wikidot.Wiki(wiki_url)
        creator = pyscp.snapshot.SnapshotCreator(dbpath=db_path, new_run=new_run)
        creator.take_snapshot(wiki=wiki, forums=forums)
        return True
    except Exception as e:
        print(e)
        return False

def extract_scp_information(wiki_url=None, scp_num=None):
    wiki = pyscp.wikidot.Wiki(wiki_url)
    p = wiki('scp-'+ str(scp_num))
    scp_data = scp.item.SCP(num=scp_num, wiki=p)
    print(scp_data.link)
    print(scp_data.title)
    print(scp_data.object_class)
    print(scp_data.containment_procedures)
    # print(scp_data.description)

def number_of_digits(num=None):
    return len(str(num))

def main():
    wiki_url = 'www.scp-wiki.net'
    db_path = 'snapshot_file.db'
    new_run = True
    # snapshot_created = download_snapshot(wiki_url=wiki_url, db_path=db_path, new_run=new_run)
    # scp = 'scp-083'
    scp = 'scp-83'

    for i in range(1, 5):
        scp_num = i
        if number_of_digits(i) == 2 or number_of_digits(i) == 1:
            scp_num = f'{i:03}'
        extract_scp_information(wiki_url=wiki_url, scp_num=scp_num)

if __name__ == "__main__":
    main()
