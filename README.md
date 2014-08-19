xmltools
========

XMLTools is Python XML tool base on XML SAX parser provide analisys and another XML manipulation instrument.

XML Statistics
--------------

Let's look example of usage:

```bash
$ xmltool test1.xml
| root.elem2.childElem2                    |        1 |
| root.elem2.childElem1                    |        1 |
| root                                     |        1 |
| root.elem2                               |        2 |
| root.py:elem1                            |        2 |
```

As you can see `xmltool` show node's count (+BONUS: support xmlns via dot notation).
