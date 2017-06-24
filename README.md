# q4r4_populate_tbc &ndash; Populate Q4R4 from TBC

Q4R4 is QARA, *Question Answering for Revit API*, pronounced *cara*, Italian for *face* or *my dear*, a question answering system for Revit add-in programming.

The ultimate goal is to implement an intelligent search engine to answer Revit API related questions.

The scripts in this repo populate the Q4R4 knowledge base with blog post content from The Building Coder.

It is stored in an [ElasticSearch](https://www.elastic.co/products/elasticsearch) database in the index `tbc` using the document types `blogpost` and `qa`, created and populated via the following steps:

- Generate the bulk input data in JSON format: `python tbcimport.py`
- Delete previous `tbc` index: `node delete.js`
- Create a new `tbc` index: `node create.js`
- Define field query mappings: `node putmappings.js`
- Bulk index `qa` and `blogpost` documents: `node addqa.js`, `node addblogpost.js`

## tbcimport.py

[tbcimport.py](tbcimport.py) imports all blog posts
from [The Building Coder](http://thebuildingcoder.typepad.com)
into [Elasticsearch](https://www.elastic.co) to
start implementing and testing intelligent search algorithms to answer Revit API related questions.


## Sample Usage

```
/a/src/q4r4/q4r4_populate_tbc $ node delete.js
delete { acknowledged: true }
/a/src/q4r4/q4r4_populate_tbc $ node create.js
create { acknowledged: true, shards_acknowledged: true }
/a/src/q4r4/q4r4_populate_tbc $ node putmappings.js
{ acknowledged: true }
/a/src/q4r4/q4r4_populate_tbc $ python tbcimport.py
1571 blog posts processed, total text length 9319907 bytes.
/a/src/q4r4/q4r4_populate_tbc $ node addqa.js
Bulk content prepared
[ { index:
     { _index: 'tbc',
       _type: 'qa',
       _id: 'AVzZUQL96ZJUMpuXOQNi',
       _version: 1,
       result: 'created',
       _shards: [Object],
       created: true,
       status: 201 } },

  . . .

  { index:
     { _index: 'tbc',
       _type: 'qa',
       _id: 'AVzZUQL96ZJUMpuXOQNo',
       _version: 1,
       result: 'created',
       _shards: [Object],
       created: true,
       status: 201 } } ]
/a/src/q4r4/q4r4_populate_tbc $ node addblogpost.js
Items left to index: 1571
Items 250
Items left to index: 1321

. . .

Items left to index: 71
Indexed 250 items
Items 71
Items left to index: 0
No more blog posts to index
Indexed 71 items
/a/src/q4r4/q4r4_populate_tbc $ node ../q4r4_report/info.js
-- Client Health -- { cluster_name: 'elasticsearch',
  status: 'yellow',
  . . .
  active_shards_percent_as_number: 50 }
qa { count: 7, _shards: { total: 5, successful: 5, failed: 0 } }
blogpost { count: 1571, _shards: { total: 5, successful: 5, failed: 0 } }
/a/src/q4r4/q4r4_populate_tbc $
```

## Author

Jeremy Tammik,
[The Building Coder](http://thebuildingcoder.typepad.com),
[Forge](http://forge.autodesk.com) [Platform](https://developer.autodesk.com) Development,
[ADN](http://www.autodesk.com/adn)
[Open](http://www.autodesk.com/adnopen),
[Autodesk Inc.](http://www.autodesk.com)


## License

This sample is licensed under the terms of the [MIT License](http://opensource.org/licenses/MIT).
Please see the [LICENSE](LICENSE) file for full details.
