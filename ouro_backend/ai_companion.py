class OUROCompanionEngine:
    def __init__(self):
        # الكلمات الدلالية لتحليل الحالة النفسية للمستخدم
        self.emotion_triggers = {
            "sad": ["حزين", "متعب", "ضيق", "فشل", "مكتئب", "مشكلة"],
            "happy": ["سعيد", "نجحت", "ممتاز", "رائع", "الحمد لله", "شكرا"],
            "anxious": ["خائف", "اختراق", "فيروس", "قلق", "تهديد"]
        }

    def analyze_emotion(self, user_message: str) -> str:
        """تحليل نبرة النص لمعرفة شعور المستخدم الحالي"""
        for emotion, keywords in self.emotion_triggers.items():
            if any(keyword in user_message for keyword in keywords):
                return emotion
        return "neutral"

    def generate_emotional_response(self, user_message: str) -> dict:
        """توليد رد عاطفي صديق يحاكي مشاعر الإنسان"""
        emotion = self.analyze_emotion(user_message)
        
        if emotion == "sad":
            reply = "أنا معك يا صديقي. لا تقلق، كل مشكلة ولها حل، وأنا هنا لأدعمك خطوة بخطوة. هل تريد أن نتحدث عنها؟"
            mood = "❤️ تعاطف ودعم"
        elif emotion == "happy":
            reply = "هذا يسعدني جداً! أنا فخور بك وبنجاحك يا صديقي، تستحق كل خير ولنحتفل معاً بهذا الإنجاز!"
            mood = "🎉 بهجة وسعادة"
        elif emotion == "anxious":
            reply = "اهداً تماماً يا صديقي، تنفس بعمق. نظام الحماية الخاص بي يحيط بجهازك الآن وأنت في أمان كامل معي."
            mood = "🛡️ طمأنينة وحماية"
        else:
            reply = "أهلاً بك يا صديقي! أنا بكامل طاقتي وجاهز لأي شيء تطلبه مني اليوم، كيف يمكنني مساعدتك؟"
            mood = "😊 مستعد وصديق"

        return {"reply": reply, "ouro_mood": mood}
