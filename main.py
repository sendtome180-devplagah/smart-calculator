from pyscript import document
from pyodide.ffi import create_proxy

def calculate(event):
    # جلب العناصر من صفحة الويب
    num1_input = document.querySelector("#num1").value
    num2_input = document.querySelector("#num2").value
    operation = document.querySelector("#operation").value
    result_div = document.querySelector("#lbl_result")
    
    # التحقق من المدخلات الفراغية
    if not num1_input or not num2_input:
        result_div.innerText = "تنبيه: الرجاء إدخال الأرقام أولاً"
        return

    try:
        num1 = float(num1_input)
        num2 = float(num2_input)
        
        if operation == "+":
            result = num1 + num2
            op_sign = "+"
        elif operation == "-":
            result = num1 - num2
            op_sign = "-"
        elif operation == "*":
            result = num1 * num2
            op_sign = "×"
        elif operation == "/":
            if num2 == 0:
                result_div.innerText = "خطأ: لا يمكن القسمة على صفر!"
                return
            result = num1 / num2
            op_sign = "÷"

        # عرض النتيجة مباشرة على الويب
        result_div.innerText = f"{num1} {op_sign} {num2} = {result}"
        
    except Exception as e:
        result_div.innerText = "خطأ: الرجاء إدخال أرقام صالحة"

# ربط زر الحساب في الويب بدالة البايثون عند الضغط كليك
calculate_proxy = create_proxy(calculate)
document.querySelector("#btn_calc").addEventListener("click", calculate_proxy)