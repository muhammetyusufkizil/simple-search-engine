# Google Custom Search API'yi içe aktarın
from googleapiclient.discovery import build

# API anahtarınızı ve arama motoru kimliğinizi girin
api_key = "YOUR_API_KEY"
cse_id = "YOUR_CSE_ID"

# Arama yapmak istediğiniz sorguyu ve sonuç sayısını girin
query = "Bing"
num_results = 10

# Arama motoru nesnesi oluşturun
service = build("customsearch", "v1", developerKey=api_key)

# Arama yapın ve sonuçları alın
results = service.cse().list(q=query, cx=cse_id, num=num_results, filter="lang_tr", sort="date").execute()

# Sonuçları markdown ile ekrana yazdırın
for item in results["items"]:
    print(f"# {item['title']}")
    print(f"[{item['link']}]({item['link']})")
    print(f"> {item['snippet']}")
    print()
