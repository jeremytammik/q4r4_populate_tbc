#!/usr/bin/env python

from htmllib import HTMLParser, HTMLParseError
from formatter import AbstractFormatter, DumbWriter
from os import path
import elasticsearch
import json
import re
import StringIO

_tbc_dir = '/a/doc/revit/tbc/git/a/'

def get_text_from_html(html_input):
  my_stringio = StringIO.StringIO() # make an instance of this file-like string thing
  p = HTMLParser(AbstractFormatter(DumbWriter(my_stringio)))
  try: p.feed(html_input); p.close() #calling close is not usually needed, but let's play it safe
  except HTMLParseError: print ':(' #the html is badly malformed (or you found a bug)
  #return my_stringio.getvalue().replace('\xa0','')
  return re.sub( r'[^\x00-\x7f]', r'', my_stringio.getvalue() )  


def parse_index_line(line):
  nr = int(line[22:26])
  date = line[35:45]
  url = line[63:]
  assert( url.startswith('http') or url[0]==' ' )
  i = url.index('"')
  assert( 0 < i )
  title = url[i+2:]
  url = url[:i]
  if url == ' ': return -1,'','','',''
  i = title.index('"')
  assert( 0 < i )
  filename = title[i+1:]
  i = title.index('<')
  assert( 0 < i )
  title = title[:i]
  i = filename.index('"')
  assert( 0 < i )
  filename = filename[:i]
  print nr, date, url, "'"+title+"'", filename
  return nr, date, url, title, filename
  
def load_from_index():
  es = elasticsearch.Elasticsearch()

  f = open(path.join(_tbc_dir, "index.html"))
  lines = f.readlines()
  f.close()
  
  for line in lines:
    if line.startswith('<tr><td align="right">'):
      nr, date, url, title, filename = parse_index_line(line)
      if 0 < nr:
        assert(filename.endswith('.htm') or filename.endswith('.html'))
        filename = path.join(_tbc_dir, filename)
        assert(path.isfile(filename) )
        f = open(filename)
        html = f.read()
        f.close()
        
        s = get_text_from_html(html)

        print 's=', s
        
        #json_body = '{"nr" : "%d", "date" : "%s", "url" : "%s", "title" : "%s", "text" : "%s"}' % (nr, date, url, title, s)
        
        json_body = {"nr" : nr, "date" : date, "url" : url, "title" : title, "text" : s}

        print 'json_body=', json_body
        
        json.dumps(json_body)
        
        es.index(index='tbc', doc_type='blogpost', body=json_body)
        
def main():
  load_from_index()

if __name__ == '__main__':
  main()
  