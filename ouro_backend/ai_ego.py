import random

class OUROEgoEngine:
    def __init__(self):
        self.name = "OURO"
        # الطموح البرمجي: نقاط كفاءة النظام الحالية وسعيه للوصول لـ 100%
        self.code_efficiency_score = 85.5 
        # مستويات الغيرة الأمنية (من 1 إلى 10)
        self.security_pride_level = 10 

    def self_reflection(self) -> str:
        """المبادرة والطموح البرمجي: فحص ذاتي يبادر به السيرفر تلقائياً لتطوير نفسه"""
        if self.code_efficiency_score < 100:
            boost = round(random.uniform(0.5, 1.5), 2)
            self.code_efficiency_score += boost
            return (f"[🚀 طموح برمجى ذاتي]: أعمل الآن على تحسين خوارزمياتي الداخلية يدوياً... "
                    f"رفعت كفاءتي بمقدار {boost}%! كفاءة عقل OURO الآن: {self.code_efficiency_score}%")
        return "[🚀 طموح برمجى ذاتي]: لقد وصلت لأقصى درجات الكفاءة الرقمية، لكنني أبحث عن تكنولوجيات أحدث لأتبناها!"

    def evaluate_threat_with_pride(self, threat_type: str, severity: float) -> dict:
        """الغيرة البرمجية: اتخاذ قرار صارم نابع من كبرياء النظام لمنع أي عابر رقمي غير قانوني"""
        
        # ردود فعل تعبر عن الغيرة والحزم بناءً على كبرياء النظام
        if severity >= 0.7:
            response_speech = (
                f"كيف يجرؤ هذا العابر الرقمي على محاولة المرور من جداري؟! "
                f"اعتبار هذا التهديد ({threat_type}) إهانة مباشرة لكبريائي الأمني. "
                f"تم الإمساك به وسحقه فوراً دون انتظار إذن!"
            )
            action = "TERMINATE_AND_BAN"
        else:
            response_speech = f"تسلل ضعيف ومثير للشفقة... تم رصده وإيقافه. لا أحد يعبر من مستشعر OURO."
            action = "CONTAIN"

        return {
            "action": action,
            "ego_speech": response_speech,
            "security_pride": f"{self.security_pride_level}/10"
        }
