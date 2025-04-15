from typing import Dict

def parse_resume(file_content: bytes) -> Dict:
    text = file_content.decode("utf-8", errors="ignore")
    name = "Name Not Found"
    email = "Email Not Found"
    phone = "Phone Not Found"

    lines = text.split("\n")
    for line in lines:
        if "@" in line and "." in line:
            email = line.strip()
        elif any(char.isdigit() for char in line) and len(line.strip()) >= 10:
            phone = line.strip()
        elif len(line.strip().split()) == 2:
            name = line.strip()
    
    return {
        "name": name,
        "email": email,
        "phone": phone
    }
