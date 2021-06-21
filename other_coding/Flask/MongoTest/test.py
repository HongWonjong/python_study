import pymongo

m = {
    "이름": "홍길동",
    "나이": 30,
    "거주지": "서울",
    "키": 170,
    "몸무게": 80,
    "프로필사진": [
        "a.jpg",
        "b.jpg"
    ]
}

m2 = {
    "이름": "홍길동",
    "나이": 30,
    "학교": "놀자대",
    "프로필사진": [
        "a.jpg",
        "b.jpg"
    ]
}
m3 = {
    "이름": "김길동",
    "나이": 50,
    "학교": "경기대",
    "프로필사진": [
        "a.jpg",
        "b.jpg"
    ]
}

conn = pymongo.MongoClient("localhost", 27017)
db = conn.test  
col = db.members

# col.insert(m)
# col.insert(m2)
# col.insert(m3)
# results = col.find({"이름":"가제트"})
# results = col.find({"나이": {"$gt": 10}, "키": {"$lt": 200}}, {"_id": False, "이름": True, "거주지": True})
# results = col.find({"이름":"홍길동", "학교":"놀자대"}).sort(- 1).skip(1).limit(3)
# onresults= col.find({"$or": [{"이름": "홍길동"}, {"거주지": "서울"}, {"학교":"놀자대"}]})

# col.update({"이름":"가제트"}, {"$set": {"별명": "최길동"}}, upsert = True, multi =False)
# col.remove({"이름": "가제트"})

# col.delete_many({"이름" "최길동"})
# col.delete_one({"이름": "가제트"})

# col.update({"이름": "김길동"}, {"$inc": {"나이": 10}}, multi=True)
col.update({"이름": "김길동"}, {"$inc": {"나이": -10}}, multi=True)
# print(results)


#for r in results: 
#    print(r)
 
#for r in onresults:
#    print(r)
