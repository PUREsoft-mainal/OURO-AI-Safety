import psutil
import time
import requests

# عنوان السيرفر السحابي (مكتمل وصحيح للتجربة المحلية حالياً)
SERVER_URL = "http://127.0.0"

def monitor_system_processes(cpu_threshold=80.0):
    print("[-] OURO-AI-Safety: جاري بدء نظام مراقبة العمليات الذكي...")
    print("--------------------------------------------------")
    
    try:
        while True:
            for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'username']):
                try:
                    cpu_usage = proc.info['cpu_percent']
                    
                    if cpu_usage > cpu_threshold:
                        print(f"[⚠️ تنبيه محلي] عملية تستهلك النظام: {proc.info['name']} ({cpu_usage}%)")
                        
                        # تجهيز البيانات لإرسالها لعقل OURO السحابي
                        payload = {
                            "pid": proc.info['pid'],
                            "name": proc.info['name'],
                            "cpu_usage": cpu_usage,
                            "username": proc.info['username'] or "unknown"
                        }
                        
                        # إرسال البيانات للسحابة فوراً
                        try:
                            response = requests.post(SERVER_URL, json=payload)
                            if response.status_code == 200:
                                ai_decision = response.json()
                                print(f"[🧠 قرار OURO السحابي]: {ai_decision['action']} - {ai_decision['reason']}")
                        except requests.exceptions.ConnectionError:
                            print("[❌ خطأ] تعذر الاتصال بسيرفر OURO السحابي.")
                        
                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                    pass
            
            time.sleep(3)
            
    except KeyboardInterrupt:
        print("\n[-] تم إيقاف نظام المراقبة.")

if __name__ == "__main__":
    monitor_system_processes(cpu_threshold=80.0)
