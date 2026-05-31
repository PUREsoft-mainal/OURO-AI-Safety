from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="OURO-AI-Safety Cloud Backend")

# نموذج البيانات المستلمة من العميل
class ProcessAlert(BaseModel):
    pid: int
    name: str
    cpu_usage: float
    username: str

@app.get("/")
def home():
    return {"status": "online", "message": "OURO Cloud Brain is running."}

@app.post("/api/v1/report-threat")
def report_threat(alert: ProcessAlert):
    print(f"[🔥 تحليل سحابي] تم استلام تنبيه من جهازك!")
    print(f"البرنامج المشبوه: {alert.name} | استهلاك المعالج: {alert.cpu_usage}%")
    
    # هنا مستقبلاً: سيقوم نموذج الذكاء الاصطناعي بفحص سلوك هذا البرنامج
    # حالياً سنضع محاكاة بسيطة لحظر البرنامج إذا تخطى استهلاكه 90%
    if alert.cpu_usage > 90.0:
        return {"action": "BLOCK", "reason": "AI Analysis: High risk malicious behavior detected."}
    
    return {"action": "MONITOR", "reason": "AI Analysis: Suspicious but keep monitoring."}
