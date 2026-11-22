"""
題號：week7-3
題名：BMI計算
描述：
請使用函式方法撰寫作業，在main()函式中輸入身高和體重，
將此身高和體重傳給一計算BMI的函式 (例: BMI(h, w))，
最後顯示BMI及代表意義。有關BMI的計算如下:
BMI = weight (kg) / height^2 (m^2)
BMI值               代表意義
BMI < 18.5          underweight
18.5 <= BMI < 25    normal
25.0 <= BMI < 30    overweight
30 <= BMI           fat
"""

# 解答
def BMI(h, w):
    message = "normal"
    BMI = w / (h / 100) ** 2
    if BMI < 18.5:
        message = "under weight"
    elif 18.5 <= BMI < 25:
        message = "normal"
    elif 25 <= BMI < 30:
        message = "over weight"
    elif 30 <= BMI:
        message = "fat"
    else:
        message = "unknown"
    
    return BMI, message

def main():
    h = int(input("Please enter height (cm): "))
    w = int(input("Please enter weight (kg): "))
    value, message = BMI(h, w)
    print("Height is %.1f, weight is %.1f, BMI = %.1f, your BMI is %s" %(h, w, value, message))

main()
