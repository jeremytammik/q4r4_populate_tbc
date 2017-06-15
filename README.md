# q4r4_populate_tbc &ndash; Populate Q4R4 from TBC

Q4R4 is QARA, *Question Answering for Revit API*, pronounced *cara*, Italian for *face* or *my dear*, a question answering system for Revit add-in programming.

This module populates the Q4R4 knowledge base with blog post content from The Building Coder.

The first module here is [tbcimport.py](tbcimport.py).
It imports all blog posts
from [The Building Coder](http://thebuildingcoder.typepad.com)
into [Elasticsearch](https://www.elastic.co) to
start implementing and testing intelligent search algorithms to answer Revit API related questions.


## Usage

Currently the following manual sequence of commands:

```
/a/src/q4r4/q4r4_populate_tbc $ node delete.js
delete { acknowledged: true }
/a/src/q4r4/q4r4_populate_tbc $ node create.js
create { acknowledged: true, shards_acknowledged: true }
/a/src/q4r4/q4r4_populate_tbc $ node putmappings.js
{ acknowledged: true }
/a/src/q4r4/q4r4_populate_tbc $ python tbcimport.py
1566 posts imported, total text length 9298881 bytes.
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
