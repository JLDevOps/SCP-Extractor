import pyscp
import re
import scp
import csv
import os

def create_csv(file='scp.csv'):
    header = ['ID', 'Item', 'Title', 'Class', 'Containment Procedures', 'Description', 'Addendum', 'Document', 'Breach Overview', 'Link']
    with open(file, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(header)
    csv_file.close()

def download_snapshot(wiki_url=None, db_path=None, forums=False, new_run=False):
    try:
        wiki = pyscp.wikidot.Wiki(wiki_url)
        creator = pyscp.snapshot.SnapshotCreator(dbpath=db_path, new_run=new_run)
        creator.take_snapshot(wiki=wiki, forums=forums)
        return True
    except Exception as e:
        return False

def get_scp_info(wiki_url=None, scp_id=None):
    wiki = pyscp.wikidot.Wiki(wiki_url)
    p = wiki('scp-'+ str(scp_id))
    scp_data = scp.item.SCP(num=scp_id, wiki=p)
    return scp_data

def extract_scp_information(wiki_url='www.scp-wiki.net', file='scp.csv', first=1, last=1000):
    # Loop through all SCPs
    with open(file, 'a', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)
        for i in range(first, last):
            scp_num = i
            num_digits = len(str(i))
            if num_digits == 1 or num_digits == 2:
                scp_num = f'{i:03}'
            scp_data = get_scp_info(wiki_url=wiki_url, scp_id=scp_num)
            csv_writer.writerow(list(scp_data))
            csv_file.flush()
 
def main():
    create_csv()
    extract_scp_information(first=1, last=5000)


if __name__ == "__main__":
    main()
