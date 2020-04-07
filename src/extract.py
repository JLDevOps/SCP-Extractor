import pyscp
import re
import scp

def download_snapshot(wiki_url=None, db_path=None, forums=False, new_run=False):
    try:
        wiki = pyscp.wikidot.Wiki(wiki_url)
        creator = pyscp.snapshot.SnapshotCreator(dbpath=db_path, new_run=new_run)
        creator.take_snapshot(wiki=wiki, forums=forums)
        return True
    except Exception as e:
        return False

def extract_scp_information(wiki_url=None, scp_num=None):
    wiki = pyscp.wikidot.Wiki(wiki_url)
    p = wiki('scp-'+ str(scp_num))
    scp_data = scp.item.SCP(num=scp_num, wiki=p)
    print(scp_data.__repr__())

def number_of_digits(num=None):
    return len(str(num))

def main():
    wiki_url = 'www.scp-wiki.net'
    
    # Loop through all SCPs
    for i in range(1, 10):
        scp_num = i
        if number_of_digits(i) == (1 or 2):
            scp_num = f'{i:03}'
        extract_scp_information(wiki_url=wiki_url, scp_num=scp_num)


if __name__ == "__main__":
    main()
