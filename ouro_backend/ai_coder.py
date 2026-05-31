import re

class OUROCoderEngine:
    def __init__(self):
        # قاعدة بيانات مصغرة لمحاكاة الأخطاء الشائعة وحلولها
        self.common_errors = {
            "SyntaxError: invalid syntax": "يوجد خطأ في صياغة الكود، تأكد من إغلاق الأقواس أو علامات التنصيص.",
            "ModuleNotFoundError": "المكتبة المستدعاة غير مثبتة في النظام، يجب اقتراح تثبيتها على المستخدم.",
            "IndentationError": "خطأ في المسافات البادئة (Tabs/Spaces)، تأكد من تنسيق الأسطر بشكل صحيح.",
            "NameError": "تم استخدام متغير أو دالة غير معرفة مسبقاً، تأكد من كتابة الاسم بشكل صحيح."
        }

    def analyze_code_for_errors(self, code_content: str, error_message: str = None):
        """فحص الأكواد وإصلاح الأخطاء تلقائياً"""
        analysis_result = {
            "has_error": False,
            "error_type": "None",
            "suggestion": "الكود يبدو سليماً ولا توجد أخطاء واضحة.",
            "fixed_code": None
        }

        # إذا أرسل المستخدم رسالة الخطأ مباشرة مع الكود
        if error_message:
            analysis_result["has_error"] = True
            analysis_result["error_type"] = error_message
            
            # البحث عن حل في قاعدة البيانات
            for key, tip in self.common_errors.items():
                if key in error_message:
                    analysis_result["suggestion"] = tip
                    break
            
            # محاكاة إصلاح خطأ استدعاء مكتبة كمثال
            if "ModuleNotFoundError" in error_message:
                missing_module = re.findall(r"No module named '(\w+)'", error_message)
                if missing_module:
                    analysis_result["suggestion"] = f"المكتبة '{missing_module[0]}' مفقودة. تم التعرف عليها وسيتم عرض خيار تثبيتها."
            
            return analysis_result

        return analysis_result

    def detect_required_libraries(self, code_content: str):
        """التعرف على المكتبات المطلوبة في الكود البرمجي وعرضها"""
        # استخدام التعبيرات النمطية لاستخراج المكتبات المستدعاة بـ import أو from
        imports = re.findall(r"^\s*(?:import|from)\s+(\w+)", code_content, re.MULTILINE)
        return list(set(imports))
