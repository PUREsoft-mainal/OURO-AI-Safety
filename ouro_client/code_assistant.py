import requests

# رابط السيرفر السحابي (المحلي مؤقتاً)
SERVER_URL = "http://127.0.0"

def use_ouro_code_assistant(user_code: str, error_msg: str = None):
    print("[-] OURO-AI-Safety: جاري إرسال الكود إلى السيرفر السحابي للتحليل...")
    print("------------------------------------------------------------------")
    
    payload = {
        "code": user_code,
        "error_log": error_msg
    }
    
    try:
        response = requests.post(SERVER_URL, json=payload)
        if response.status_code == 200:
            result = response.json()
            
            # 1. عرض نتائج تحليل الأخطاء
            analysis = result["analysis"]
            if analysis["has_error"]:
                print(f"[❌ تم كشف خطأ برمجى]: {analysis['error_type']}")
                print(f"[💡 اقتراح إصلاح OURO]: {analysis['suggestion']}")
            else:
                print(f"[✅ فحص آمن]: {analysis['suggestion']}")
                
            # 2. عرض المكتبات المطلوبة
            libraries = result["detected_libraries"]
            if libraries:
                print(f"\n[📚 المكتبات المطلوبة المكتشفة في الكود]: {', '.join(libraries)}")
                print("[⚙️ نظام التثبيت الذاتي]: هل تود أن يقوم OURO بتثبيت هذه المكتبات لك تلقائياً؟ (نعم/لا)")
                
        else:
            print("[❌ خطأ] فشل السيرفر في تحليل الكود.")
    except requests.exceptions.ConnectionError:
        print("[❌ خطأ] تعذر الاتصال بسيرفر OURO السحابي حالياً.")

if __name__ == "__main__":
    # كود تجريبي يحتوي على مكتبات مفقودة وخطأ محاكاة لتجربة النظام
    sample_code = """
    import numpy as np
    import requests
    print("Hello OURO Project")
    """
    sample_error = "ModuleNotFoundError: No module named 'numpy'"
    
    # تشغيل المساعد البرمجي التجريبي
    use_ouro_code_assistant(sample_code, sample_error)
