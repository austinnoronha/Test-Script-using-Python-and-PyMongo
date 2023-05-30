import pymongo

print("Script start....")

DATABASE_NAME = "_______DBNAME________"
DATABASE_HOST = "______IP______"

DATABASE_USERNAME = "root"
DATABASE_PASSWORD = "root"

COLLECTION_NAME_A = "my_collection"

try:
	print("[+] Connecting....DATABASE_HOST", DATABASE_HOST, DATABASE_NAME)
  myclient = pymongo.MongoClient('mongodb://%s:%s@%s/%s' % (DATABASE_USERNAME, DATABASE_PASSWORD, DATABASE_HOST, DATABASE_NAME))

	print("[+] Connecting....DATABASE_USERNAME", DATABASE_USERNAME)
  myclient.test.authenticate( DATABASE_USERNAME , DATABASE_PASSWORD )
	
  print("[+] Connecting....success!")

	print("[+] Client select database ", DATABASE_NAME)
  mydb = myclient[DATABASE_NAME]

  print("[+] Database print all collections....!")
  collection = mydb.collection_names(include_system_collections=False)
  for collect in collection:
    print("[+] Collection name.... ", collect)
  
  print("[+] Database print all documents in a collection....", COLLECTION_NAME_A)

  coll = mydb[COLLECTION_NAME_A]
  cursor = coll.find({})
  for document in cursor:
    print("[+] Collection document print", document)
      
  print("[+] Collection done...!")  
except Exception as e:
    print("[+] Database connection error!")
    raise e
	
	
print("Script end!")
