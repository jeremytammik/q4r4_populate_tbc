#!/usr/bin/env python

import elasticsearch

_tbc_index = 'tbc'
_tbc_doc_type = 'blogpost'

def delete_index():
  "Delete all The Building Coder blog posts from Elasticsearch."
  es = elasticsearch.Elasticsearch()
  
  try:
    count = es.count(_tbc_index, _tbc_doc_type)['count']
    print count, 'tbc blog post documents'
  except:
    print 'Not an index:', _tbc_index

  es.indices.delete( index=_tbc_index, ignore=[400, 404] )

def main():
  delete_index()

if __name__ == '__main__':
  main()
