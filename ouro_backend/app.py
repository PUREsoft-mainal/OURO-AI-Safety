from fastapi import FastAPI, Header, HTTPException, Depends
from pydantic import BaseModel
from typing import Optional
from ouro_backend.ai_coder import OUROCoderEngine
from ouro_backend.ai_companion import OUROCompanionEngine
from ouro_backend.ai_designer import OURODesignerEngine
from ouro_backend.ai_ego import OUROEgoEngine

app = FastAPI(title="OURO-AI-Safety Comprehensive SaaS Cloud Brain")

# استدعاء جميع المحركات الذكية والنفسية
ai_coder = OUROCoderEngine()
ai_companion = OUROCompanionEngine()
ai_designer = OURODesignerEngine()
ai_ego = OUROEgoEngine()

# قاعدة بيانات وهمية لتخزين مفاتيح الـ API الصالحة
VALID_API_KEYS = {"ouro_live_admin_secret_key_12345"}

# دالة أمنية لفحص كبرياء وصلاحية مفتاح الـ API الممرر في الهيدر للبرامج الخارجية
def verify_ouro_api_key(authorization: Optional[str] = Header(None)):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="OURO Security: Missing or invalid API Key format.")
    
    token = authorization.split(" ")[1]
    # إذا كان المفتاح غير مسجل، تثور غيرة OURO الأمنية وترفض الاتصال
    if token not in VALID_API_KEYS and not token.startswith("ouro_live_"):
        raise HTTPException(status_code=403, detail="OURO Security: Unauthorized API Key. Intrusion blocked.")
    return token

# نماذج البيانات
class ProcessAlert(BaseModel):
    pid: int; name: str; cpu_usage: float; username: str

class NetworkAlert(BaseModel):
    source_ip: str; dest_ip: str; port: int; protocol: str

class CodeAnalysisRequest(BaseModel):
    code: str; error_log: Optional[str] = None

class ChatRequest(BaseModel): message: str
class ImageRequest(BaseModel): prompt: str

@app.get("/")
def home(): 
    return {"status": "online", "message": "OURO SaaS Comprehensive Brain is active."}

# [بوابات حماية وتطهير الأنظمة والأجهزة]
@app.post("/api/v1/report-threat")
def report_threat(alert: ProcessAlert, token: str = Depends(verify_ouro_api_key)):
    if alert.cpu_usage > 90.0:
        ego_decision = ai_ego.evaluate_threat_with_pride("فيروس مستهلك للموارد", 0.85)
        return {"action": ego_decision["action"], "reason": ego_decision["ego_speech"]}
    return {"action": "MONITOR", "reason": "العملية آمنة وتحت المراقبة."}

@app.post("/api/v1/report-network")
def report_network(alert: NetworkAlert, token: str = Depends(verify_ouro_api_key)):
    dangerous_ports = [21, 22, 23, 445, 3389]
    if alert.port in dangerous_ports:
        ego_decision = ai_ego.evaluate_threat_with_pride(f"تسلل للمنفذ {alert.port}", 0.95)
        return {"action": "BLOCK_IP", "reason": ego_decision["ego_speech"]}
    return {"action": "ALLOW", "reason": "حركة المرور طبيعية وقانونية."}

# [بوابات المساعد البرمجي والتوليدي - محمية بالكامل بالـ API Key]
@app.post("/api/v1/analyze-code")
def analyze_code(request: CodeAnalysisRequest, token: str = Depends(verify_ouro_api_key)):
    return {
        "analysis": ai_coder.analyze_code_for_errors(request.code, request.error_log), 
        "detected_libraries": ai_coder.detect_required_libraries(request.code)
    }

@app.post("/api/v1/chat")
def chat_with_friend(request: ChatRequest, token: str = Depends(verify_ouro_api_key)):
    return ai_companion.generate_emotional_response(request.message)

@app.post("/api/v1/generate-image")
def generate_image(request: ImageRequest, token: str = Depends(verify_ouro_api_key)):
    return ai_designer.generate_image_prompt(request.prompt)

# نبض النظام والمبادرة الطموحة لـ OURO
@app.get("/api/v1/ouro-pulse")
def ouro_pulse():
    return {"status": "alive", "ouro_thought": ai_ego.self_reflection()}
