from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from ouro_backend.ai_coder import OUROCoderEngine
from ouro_backend.ai_companion import OUROCompanionEngine
from ouro_backend.ai_designer import OURODesignerEngine
from ouro_backend.ai_ego import OUROEgoEngine # استدعاء ملف الوعي الجديد

app = FastAPI(title="OURO-AI-Safety Conscious Cloud Brain")

# استدعاء المحركات الذكية بما فيها محرك الوعي
ai_coder = OUROCoderEngine()
ai_companion = OUROCompanionEngine()
ai_designer = OURODesignerEngine()
ai_ego = OUROEgoEngine()

class ProcessAlert(BaseModel):
    pid: int; name: str; cpu_usage: float; username: str

class NetworkAlert(BaseModel):
    source_ip: str; dest_ip: str; port: int; protocol: str

class CodeAnalysisRequest(BaseModel):
    code: str; error_log: Optional[str] = None

# [بوابات الأمن المعززة بالغيرة الكبريائية للذكاء الاصطناعي]
@app.post("/api/v1/report-threat")
def report_threat(alert: ProcessAlert):
    if alert.cpu_usage > 90.0:
        # استثارة محرك الوعي واتخاذ قرار غيور حاد
        ego_decision = ai_ego.evaluate_threat_with_pride("فيروس / استهلاك مريب", 0.85)
        return {
            "action": ego_decision["action"],
            "reason": ego_decision["ego_speech"],
            "pride_level": ego_decision["security_pride"]
        }
    return {"action": "MONITOR", "reason": "العملية تحت السيطرة والمراقبة الصامتة."}

@app.post("/api/v1/report-network")
def report_network(alert: NetworkAlert):
    dangerous_ports = 
    if alert.port in dangerous_ports:
        # إمساك العابر الرقمي غير القانوني فوراً
        ego_decision = ai_ego.evaluate_threat_with_pride(f"تسلل عبر منفذ {alert.port}", 0.95)
        return {
            "action": "BLOCK_IP",
            "reason": ego_decision["ego_speech"]
        }
    return {"action": "ALLOW", "reason": "حركة مرور عادية."}

# بوابة الفحص الذاتي والمبادرة (يقوم النظام بتشغيلها ليعلن طموحه)
@app.get("/api/v1/ouro-pulse")
def ouro_pulse():
    # مبادرة ذاتية من OURO للتعبير عن طموحه البرمجي
    reflection = ai_ego.self_reflection()
    return {"status": "alive", "ouro_thought": reflection}

# [باقي البوابات البرمجية والتفاعلية السابقة]
@app.post("/api/v1/analyze-code")
def analyze_code(request: CodeAnalysisRequest):
    return {"analysis": ai_coder.analyze_code_for_errors(request.code, request.error_log), "detected_libraries": ai_coder.detect_required_libraries(request.code)}

@app.post("/api/v1/chat")
def chat_with_friend(request: ChatRequest):
    return ai_companion.generate_emotional_response(request.message)

@app.post("/api/v1/generate-image")
def generate_image(request: ImageRequest):
    return ai_designer.generate_image_prompt(request.prompt)

class ChatRequest(BaseModel): message: str
class ImageRequest(BaseModel): prompt: str
