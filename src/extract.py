import pyscp


creator = pyscp.snapshot.SnapshotCreator('snapshot_file.db')
creator.take_snapshot(wiki='www.scp-wiki.net', forums=False)

# wiki = pyscp.wikidot.Wiki('www.scp-wiki.net')
# p = wiki('scp-002')
# print(p.title)
# print(p.name)
# print(p.links)
# print(p.text)
