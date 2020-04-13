import pyscp
import re
import scp
import csv
import os
import argparse

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

def get_scp_info(wiki_url=None, scp_id=None, wiki=None):
    try:
        p = wiki('scp-'+ str(scp_id))
    except:
        p = None
    
    if wiki:
        scp_data = scp.item.SCP(num=scp_id, wiki=p)
    else:
        scp_data = scp.item.SCP(num=scp_id, wiki=p)
    return scp_data

def extract_to_csv(wiki_url='www.scp-wiki.net', file='scp.csv', first=1, last=6000):
    # Loop through all SCPs
    wiki = pyscp.wikidot.Wiki(wiki_url)
    with open(file, 'a', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)
        for i in range(first, last):
            scp_num = i
            num_digits = len(str(i))
            if num_digits == 1 or num_digits == 2:
                scp_num = f'{i:03}'
            scp_data = get_scp_info(wiki_url=wiki_url, scp_id=scp_num, wiki=wiki)
            csv_writer.writerow(list(scp_data))
            csv_file.flush()

def extract_to_raw_txt(wiki_url='www.scp-wiki.net', file='scp.txt', first=1, last=6000):
    wiki = pyscp.wikidot.Wiki(wiki_url)
    with open(file, 'w', newline='', encoding='utf-8') as txt_file:
        for i in range(first, last):
            scp_num = i
            num_digits = len(str(i))
            if num_digits == 1 or num_digits == 2:
                scp_num = f'{i:03}'
            scp_data = get_scp_info(wiki_url=wiki_url, scp_id=scp_num, wiki=wiki)
            
            txt_file.writelines('<start-scp>\n')

            try:
                scp_title = 'Title: ' + scp_data.title + '\n'
            except:
                scp_title = ''
            
            try:
                scp_class = 'Class: ' + scp_data.object_class + '\n'
            except:
                scp_class = ''
            
            try:
                scp_containment = 'Special Containment Procedures: ' + scp_data.containment_procedures + '\n'
            except:
                scp_containment = ''
            
            try:
                scp_description = 'Description: ' + scp_data.description + '\n'
            except:
                scp_description = ''
            
            scp_text = scp_title + scp_class + scp_containment + scp_description
            txt_file.write(scp_text)
            txt_file.writelines('<end-scp>\n')
 
def main():
    parser = argparse.ArgumentParser(description='SCP Extraction (into a csv or print)')
    parser.add_argument('-f', '--first', help='Starting at which SCP number', required=False)
    parser.add_argument('-l', '--last', help='Last SCP number', required=False)
    parser.add_argument('-c', '--csv', help='Exports a csv file from the results', required=False)
    parser.add_argument('-t', '--text', help='Export to text file from the results', required=False)

    args = vars(parser.parse_args())
    first_num = int(args['first']) if args['first'] else None
    last_num = int(args['last']) if args['last'] else None
    csv_name = args['csv'] if args['csv'] else None
    txt_name = args['text'] if args['text'] else None
    
    if csv_name:
        create_csv(file=csv_name)
        extract_to_csv(file=csv_name, first=first_num, last=last_num)
    
    if txt_name:
        extract_to_raw_txt(file=txt_name, first=first_num, last=last_num)

if __name__ == "__main__":
    main()
