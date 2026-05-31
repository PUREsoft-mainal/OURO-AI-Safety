import requests
from scapy.all import sniff, IP, TCP

# رابط السيرفر السحابي الخاص بفحص الشبكة
SERVER_URL = "http://127.0.0"

def packet_callback(packet):
    # التأكد من أن الحزمة تحتوي على بروتوكول الإنترنت IP وبروتوكول TCP
    if packet.haslayer(IP) and packet.haslayer(TCP):
        source_ip = packet[IP].src
        dest_ip = packet[IP].dst
        port = packet[TCP].dport
        
        # تجهيز البيانات لإرسالها للسحابة لفحصها
        payload = {
            "source_ip": str(source_ip),
            "dest_ip": str(dest_ip),
            "port": int(port),
            "protocol": "TCP"
        }
        
        try:
            # إرسال التنبيه إلى السيرفر السحابي لـ OURO
            response = requests.post(SERVER_URL, json=payload)
            if response.status_code == 200:
                ai_decision = response.json()
                # إذا قرر السيرفر السحابي حظر الاتصال
                if ai_decision["action"] == "BLOCK_IP":
                    print(f"[🔥 حظر أمني من OURO]: تم كشف محاولة تسلل مريبة! القرار: {ai_decision['reason']}")
                else:
                    print(f"[🌐 مراقبة الشبكة]: اتصال طبيعي ومسموح به عبر منفذ {port}")
        except requests.exceptions.ConnectionError:
            # في حال عدم تشغيل السيرفر حالياً يتم تخطي الخطأ
            pass

def start_network_monitoring():
    print("[-] OURO-AI-Safety: جاري بدء نظام جدار الحماية ومراقبة حزم الشبكة الذكي...")
    print("----------------------------------------------------------------------")
    # بدء فحص كرت الشبكة مباشرة
    sniff(prn=packet_callback, store=0)

if __name__ == "__main__":
    start_network_monitoring()
