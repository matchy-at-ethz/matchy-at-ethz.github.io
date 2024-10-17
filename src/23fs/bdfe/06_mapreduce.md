# MapReduce

In MapReduce, the input data, intermediate data, and output data are all made of a large collection of **key-value pairs** (with the keys not necessarily unique, and not necessarily sorted by key)

The types of the keys and values are known at compile-time (<u>statically</u>), and they <u>do not need to be the same across all three collections</u>.

## Combine

In addition to the map function and the reduce function, the
user can supply a combine function. This combine function can then be called by the system during the map phase as many times as it sees fit to “compress” the intermediate key-value pairs. Strategically, the combine function is likely to be called at every flush of key-value pairs to a Sequence File on disk, and at every compaction of several Sequence Files into one.
However, there is no guarantee that the combine function will be
called at all, and there is also no guarantee on how many times it will be called. Thus, if the user provides a combine function, it is important that they think carefully about a combine function that does not affect the correctness of the output data. In fact, in most of the cases, the combine function will be identical to the reduce function, which is generally possibly if the intermediate key-value pairs have the same type as the output key-value pairs, and the reduce function is both associative and commutative. This is the case for summing values as well as for taking the maximum or the minimum, but not for an unweighted average (why?). As a reminder, associativity means that (a +b)+c = a +(b +c) and commutativity means that a +b = b +a.

## Terms!!

### "function"

A map function is a mathematical, or programmed, function that
takes **one** input key-value pair and returns **zero**, **one** or **more** intermediate key-value pairs.

A reduce function is a mathematical, or programmed, function that
takes **one or more** intermediate key-value pairs and returns **zero**, **one** or **more** output key-value pairs.

A combine function is a mathematical, or programmed, function
that takes **one or more** intermediate key-value pairs and returns **zero**, **one** or **more** intermediate key-value pairs.

### "task"

A map **task** is an assignment (or “homework”, or “TODO”) that consists in a (**sequential**) series of calls of the <u>map function</u> on a subset of the input. There is <u>one map task for every input split</u>, so that there are many map tasks as partitions of the input.

A reduce task is an assignment that consists in a (**sequential**) series
of calls of the <u>reduce function</u> on a subset of the intermediate input. There are as many reduce tasks as <u>partitions of the list of intermediate key-value pairs.</u>

**There is no parallelism at all within a task**!!!

Calls of the combine function are not planned as a task, but is called ad-hoc during flushing and compaction.

### "slots"

Resources (CPU and RAM) used to process one or more tasks.

**There is no parallelism within a slot**!!!

### "phase"

The map phase thus consists of several map slots processing map tasks in parallel, and the reduce phase consists of several reduce slots processing reduce tasks in parallel.
