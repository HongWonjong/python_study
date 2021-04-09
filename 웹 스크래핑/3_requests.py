import requests
res = requests.get("http://google.com")
res.raise_for_status()
#print("응답코드:", res.status_code)


#if res.status_code == 200:
#    print("정상입니다.")
#else:
#    print("html 문서 정보를 가져오는 데 문제가 생겼습니다.")

print(len(res.text))
print(res.text)

with open("google_html.html", "w", encoding = "utf8") as file:
    file.write(res.text)
