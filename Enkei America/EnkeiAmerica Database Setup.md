1.  Get Sql dump file of Locallabs.
2.  Create a new server in MySql.
3.  ![creating connection 1](https://user-images.githubusercontent.com/102354574/163122915-db7f0780-45ea-4e83-85ef-2919a4c1eafb.png)
4. ![creating connection 2](https://user-images.githubusercontent.com/102354574/163123050-5b09f751-9f55-492f-8246-14201e6c6056.png) 
5.  Create a new Database (locallab) in the newly created server. 
        \# create databse locallab;
        ![creating connection 3](https://user-images.githubusercontent.com/102354574/163123332-2fa3726f-3f78-4f51-810f-20de19a5f79c.png)
4.  Refresh the Schema (for checking if database exists or not).
5.  ![creating connection 4](https://user-images.githubusercontent.com/102354574/163123464-c21c6e0a-df0f-4edd-802f-ae3aa1777e9b.png)
6.  click on Server option (6 on navigation bar).
        Server -\> 
        Data Import -\>
        ![Data import 1](https://user-images.githubusercontent.com/102354574/163123633-346b2d7e-54be-4099-8757-af6c9300945a.png)
        Import from Disk -\> 
        Import from Self-Contained File (Select second Radio-Button) -\> 
        Select downloaded SQL Dump file (downloaded in Step 1) -\>
        ![Data import 2](https://user-images.githubusercontent.com/102354574/163123733-3dbb3de3-17bc-4f49-b413-e1fdca8bd346.png)
        Select Default Target Schema (drop down menu), (step 3) -\>
        ![Data import 3](https://user-images.githubusercontent.com/102354574/163123898-3c1c848d-f64c-4709-bc87-fc0490b8d706.png) 
        Select Start import button (bottom of dialog box).
        ![Data import 4](https://user-images.githubusercontent.com/102354574/163123988-f8b62052-0682-43e0-9ddb-64db60bce115.png)
6.  Refresh the SCHEMAS.
7.  ![Data import 5](https://user-images.githubusercontent.com/102354574/163124075-5a39448e-7d2b-411d-8d84-d518cf29acae.png)
8.  All the data will be added to the locallab database.










