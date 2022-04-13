1.  Get Sql dump file of Locallabs.
2.  Create a new server in MySql.
3.  Create a new Database (locallab) in the newly created server. \#
    create databse locallab;
4.  Refresh the Schema (for checking if database exists or not).
5.  click on Server option (6 on navigation bar). Server -\> Data Import
    -\> Import from Disk -\> Import from Self-Contained File (Select
    second Radio-Button) -\> Select downloaded SQL Dump file (downloaded
    in Step 1) -\> Select Default Target Schema (drop down menu),
    (step 3) -\> Click on Import Progress (next to Import from Disk) -\>
    Select Start import button (bottom of dialog box).
6.  Refresh the SCHEMAS.
7.  All the data will be added to the locallab database.
