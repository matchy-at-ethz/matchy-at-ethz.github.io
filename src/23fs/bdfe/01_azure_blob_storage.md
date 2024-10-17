# Azure Blob Storage

Azure Storage uses a combination of *account ID*, *partition ID* and *blob ID* to uniquely identify a blob. (S3 uses *bucket ID* and *object ID*.)

## Storage Stamp

On the physical level, Azure Blob Storage is organized in
**storage stamp**s located in various data centers worldwide.

Each storage stamp consists of 10 to 20 racks, with each rack containing around 18 storage nodes (the disks + servers).

In all, a storage stamp can store up to ca. 30 PB of data.

However, a storage stamp will not be filled more than 80% of its total capacity in order to avoid being full: if a storage stamp reaches capacity, then some data is going to be reallocated to another storage stamp in the background. And if there are not enough storage stamps, well new racks will need to be purchased and installed at the locations that make the most sense.

## Types of blobs

3 types of blobs: *block blobs*, *append blobs*, *page blobs*.

Type of blob cannot be changed after creation.

All blobs reflect committed changes immediately. Versioning is maintained via *ETag*.

### Block Blobs

Optimized for uploading large amounts of data efficiently.

Can be updated only at the granularity of an entire block.

### Page blobs

A collection of 512-byte pages optimized for *random read and write operations*.

### Append blobs

Composed of blocks like block blobs, but are optimized for *append operations*.

Blocks are added to the end of the blob only.

An append blob **does not expose its block IDs**.
