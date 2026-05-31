from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from ouro_backend.ai_coder import OUROCoderEngine

app = FastAPI(title="OURO-AI-Safety Cloud Backend")
ai_coder = OUROCoderEngine()

# نماذج الحماية والشبكة السابقة
class ProcessAlert(BaseModel):
    pid: int
    name: str
    cpu_usage: float
    username: str

class NetworkAlert(BaseModel):
    source_ip: str
    dest_ip: str
    port: int
    protocol: str

# نماذج المساعد البرمجي الجديدة
class CodeAnalysisRequest(BaseModel):
    code: str
    error_log: Optional[str] = None

@app.get("/")
def home():
    return {"status": "online", "message": "OURO Cloud Brain is running."}

# [بوابات الحماية والأمن]
@app.post("/api/v1/report-threat")
def report_threat(alert: ProcessAlert):
    if alert.cpu_usage > 90.0:
        return {"action": "BLOCK", "reason": "AI Analysis: High risk behavior."}
    return {"action": "MONITOR", "reason": "Safe."}

@app.post("/api/v1/report-network")
def report_network(alert: NetworkAlert):
    dangerous_ports = [21, 22, 23, 445, 3389]
    if alert.port in dangerous_ports:
        return {"action": "BLOCK_IP", "reason": f"AI Firewall: Vulnerable port {alert.port}."}
    return {"action": "ALLOW", "reason": "Normal traffic."}

# [بوابات المساعد البرمجي الجديد]
@app.post("/api/v1/analyze-code")
def analyze_code(request: CodeAnalysisRequest):
    print("[🧠 تحليل برمجى سحابي] تم استلام كود برمجى للفحص والتصحيح...")
    
    # فحص الأخطاء وإصلاحها
    analysis = ai_coder.analyze_code_for_errors(request.code, request.error_log)
    # كشف المكتبات المطلوبة
    libraries = ai_coder.detect_required_libraries(request.code)
    
    return {
        "analysis": analysis,
        "detected_libraries": libraries
    }
