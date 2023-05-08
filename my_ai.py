import openai
#import json

# 设置 OpenAI API 密钥
openai.api_key = "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"

# 输入文本
prompt = "hello jzq"

print("开始请求")

# 调用 OpenAI API 生成文本
response = openai.Completion.create(
  engine="text-davinci-003",
  prompt=prompt,
  max_tokens=1024,
  n=1,
  stop=None,
  temperature=0.5,
)
print("请求完成，等待回应")
# 获取 API 返回的生成文本
generated_text = response.choices[0].text

# 输出生成的文本
print(generated_text)
