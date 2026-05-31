from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from ouro_backend.ai_coder import OUROCoderEngine
from ouro_backend.ai_companion import OUROCompanionEngine
from ouro_backend.ai_designer import OURODesignerEngine

app = FastAPI(title="OURO-AI-Safety Complete Cloud Brain")

# استدعاء المحركات الذكية
ai_coder = OUROCoderEngine()
ai_companion = OUROCompanionEngine()
ai_designer = OURODesignerEngine()

# نماذج البيانات
class ProcessAlert(BaseModel):
    pid: int; name: str; cpu_usage: float; username: str

class NetworkAlert(BaseModel):
    source_ip: str; dest_ip: str; port: int; protocol: str

class CodeAnalysisRequest(BaseModel):
    code: str; error_log: Optional[str] = None

class ChatRequest(BaseModel):
    message: str

class ImageRequest(BaseModel):
    prompt: str

@app.get("/")
def home(): return {"status": "online", "message": "OURO Complete Brain is active."}

# [1. بوابات الأمن والحماية]
@app.post("/api/v1/report-threat")
def report_threat(alert: ProcessAlert):
    if alert.cpu_usage > 90.0: return {"action": "BLOCK", "reason": "AI Analysis: High risk."}
    return {"action": "MONITOR", "reason": "Safe."}

@app.post("/api/v1/report-network")
def report_network(alert: NetworkAlert):
    if alert.port in : return {"action": "BLOCK_IP", "reason": "AI Firewall: Dangerous port."}
    return {"action": "ALLOW", "reason": "Normal traffic."}

# [2. بوابات المساعد البرمجي]
@app.post("/api/v1/analyze-code")
def analyze_code(request: CodeAnalysisRequest):
    return {"analysis": ai_coder.analyze_code_for_errors(request.code, request.error_log), "detected_libraries": ai_coder.detect_required_libraries(request.code)}

# [3. بوابات الشخصية الصديقة وتوليد الصور الجديدة]
@app.post("/api/v1/chat")
def chat_with_friend(request: ChatRequest):
    print(f"[💬 دردشة إنسانية] السيرفر يتفاعل مع المستخدم كصديق...")
    return ai_companion.generate_emotional_response(request.message)

@app.post("/api/v1/generate-image")
def generate_image(request: ImageRequest):
    print(f"[🎨 طلب فني] السيرفر يقوم بإنتاج رسمة ذكية...")
    return ai_designer.generate_image_prompt(request.prompt)
