# HBase (Wide Column Store)

## `HBase` commands

`HBase` supports four kinds of low-level queries: `get`, `put`, `scan` and `delete`. Unlike a traditional key-value store, HBase also supports querying ranges of row IDs and ranges of timestamps.

```bash
put '<name_space:table_name>', '<row_key>' '<cf:column_name>', '<value>'
```

**Table name** and **column family (cf)** must be known in advance.

## `HFile`

A flat list of KeyValues, one per *cell* in the table.
The KeyValues are sorted (first by row ID, then by column family, then by column qualifier, then by version (recent to old)).

This means <u>all versions of a give cell that are in the same `HFile` are located together</u>.

The KeyValues within an `HFile` are <u>organized in blocks</u> called `HBlocks`. They have a size of 64kB but if the last KeyValue is larger than 64kB, then the block will be larger.

The `HFile` also contains an index of all blocks with their key boundaries. The index is loaded in memory prior to reading anything from the `HFile` and is kept in memory to speed up reads.

### Log-structured merge trees

`HBase` first store cells in memory (`MemStore`) as long as there is enough memory available. Once the memory is full, the `MemStore` is flushed to disk as an `HFile`. Upon flushing, all cells are written sequentially to a new HFile in ascending key order, HBlock by HBlock, concurrently building the index structure.

After many flushes, the number of `HFile`s to read from grows and
becomes impracticable. For this reason, there is an additional process called compaction that takes several `HFiles` And outputs a single, merged `HFile`. Since the cells within each `HFile` are already sorted, this can be done in linear time, as this is essentially the merge part of the merge-sort algorithm.

**The merge happens like the game 2048!!**
