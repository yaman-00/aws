import json

# قراءة ملف JSON
with open("config.json", "r") as f:
    json_data = json.load(f)
    print("JSON Data:", json_data["server_name"])

# ملاحظة: لقراءة YAML نحتاج لمكتبة خارجية (PyYAML)، لكن كمبدأ تنسيقي فهمنا شكلها وكيفية كتابتها في السيرفرات.o

