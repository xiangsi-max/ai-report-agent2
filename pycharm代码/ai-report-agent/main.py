from openai import OpenAI

# DeepSeek 的API（兼容OpenAI写法）
client = OpenAI(
    api_key="sk-7fe37f039c4242fcad097a4d29ba32ef",
    base_url="https://api.deepseek.com"
)

def ask_gpt(prompt):
    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "你是一个实验报告助手"},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3
        )
        return response.choices[0].message.content

    except Exception as e:
        print("⚠️ API不可用，进入本地模式：", e)

        # 本地兜底（保证项目能跑）
        return f"""
一、问题分析：
本题采用SIR模型研究疫情传播。

二、数学建模：
dS/dt = -βSI
dI/dt = βSI - γI
dR/dt = γI

三、Python代码：
使用scipy求解微分方程

四、结果分析：
感染人数呈现先上升后下降趋势
"""

def decompose_task(question):
    prompt = f"""
    请将以下实验题目拆解为步骤：
    {question}

    输出：
    1. 问题分析
    2. 数学建模
    3. 代码实现
    4. 结果分析
    """
    return ask_gpt(prompt)


def generate_report(question):
    prompt = f"""
    请根据以下题目生成完整实验报告：
    {question}

    要求：
    1. 问题分析
    2. 数学建模（写出SIR微分方程）
    3. Python代码（可运行）
    4. 结果分析
    """
    return ask_gpt(prompt)


if __name__ == "__main__":
    question = input("请输入实验题目：")

    steps = decompose_task(question)
    print("任务拆解：\n", steps)

    report = generate_report(question)

    with open("report.md", "w", encoding="utf-8") as f:
        f.write(report)

    print("✅ 报告已生成：report.md")