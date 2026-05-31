import requests

# روابط السيرفر السحابي (المحلي مؤقتاً)
CHAT_URL = "http://127.0.0"
IMAGE_URL = "http://127.0.0"

def talk_to_ouro(user_text: str):
    """إرسال رسالة دردشة عاطفية"""
    try:
        response = requests.post(CHAT_URL, json={"message": user_text})
        if response.status_code == 200:
            data = response.json()
            print(f"\n[حالة OURO النفسية]: {data['ouro_mood']}")
            print(f"[🤖 OURO]: {data['reply']}")
    except requests.exceptions.ConnectionError:
        print("[❌ خطأ] تعذر الاتصال بصديقك الذكي OURO.")

def ask_ouro_to_draw(prompt_text: str):
    """طلب رسم صورة من الذكاء الاصطناعي"""
    try:
        response = requests.post(IMAGE_URL, json={"prompt": prompt_text})
        if response.status_code == 200:
            data = response.json()
            print(f"\n[🎨 رد المصمم OURO]: {data['message']}")
            print(f"[🖼️ الوصف المطور]: {data['enhanced_prompt']}")
            print(f"[🔗 رابط الصورة]: {data['image_url']}")
    except requests.exceptions.ConnectionError:
        print("[❌ خطأ] تعذر الاتصال بمحرك الصور السحابي لـ OURO.")

if __name__ == "__main__":
    print("=== تجربة واجهة OURO-AI-Safety الإنسانية والإبداعية ===")
    
    # 1. تجربة التفاعل الإنساني العاطفي (محاكاة الحزن)
    print("\n[-] المستخدم: أنا حزين جداً اليوم ولم ينجح الكود الخاص بي...")
    talk_to_ouro("أنا حزين جداً اليوم ولم ينجح الكود الخاص بي")
    
    # 2. تجربة التفاعل الإبداعي (طلب رسم)
    print("\n[-] المستخدم: ارسم لي رائد فضاء يركب خيلاً على كوكب المريخ")
    ask_ouro_to_draw("رائد فضاء يركب خيلاً على كوكب المريخ")
