import re

pattern = "^พัสดุ|พัสดุ|พัสดุ$"

def service_type(sentimentText):
  if re.findall(pattern,sentimentText) or re.match(pattern, sentimentText):
    return "บริการ"
  else:
    return "อื่นๆ"

print(service_type("อิอิ"))


