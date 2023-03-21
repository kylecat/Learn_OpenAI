import openai

openai.api_key = "sk-*******************************" # 要去OpenAI的網站那邊抓API key

# list models
models = openai.Model.list()

# print the first model's id
# models_list = models.data
# for _model in models_list:
#     print(_model.id)

# gpt-3.5-turbo
completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content":"嗨"}
    ]
)

# "choices"=[{回覆狀態(finish_reason), 序號(index), 訊息(message):內容(content), 訊息:角色(role)：助手(assistant)}]
# "created"
# "id"
# "object"
# "usage" : tokens 使用情況

print("[Bot content]\t", completion.choices[0].message.content)
print("[Bot role]\t", completion.choices[0].message.role)

