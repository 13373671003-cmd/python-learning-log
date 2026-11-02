# policy = {      #policy是一个字典（dict），{}就是字典，里面是[键:值]
#     "daily_budget": 50,    
#     "models": ["gpt-x","deepseek"],
# }
# print(policy["daily_budget"])   #字典取数据：字典变量["键名字"]
# print(policy["models"][1])      #拿到列表["gpt-x","deepseek"]，然后后面加[1]：列表索引

# print("gpt-x" in policy["models"])
# print("claud" in policy["models"])

policy = {      #1. 字典部分：policy保存规则：日预算50，允许的模型列表["gpt-x","deepseek"]
    "daily_budget": 50,
    "single_limit": 10,  #单笔请求最多不能超过10（单次调用上线）
    "models": ["gpt-x","deepseek"],
}
   #2. input()等待你在终端打字，返回文本字符串   float()：把输入的文字数字(比如"100")转换成数字100.0，这样才能大小比较
spent_today = float(input("今天已经花了多少："))
cost = float(input("请输入金额："))
model = input("请输入模型：")

remaining = policy["daily_budget"] - spent_today - cost
if model not in policy["models"]:   #if not：不在里面，（放在第一个判断，拦截非法模型）
    print("拒绝：模型不在白名单")
elif cost > policy["single_limit"]:  #elif:只有上面if不成立（只有模型是合法的），才会走到这一行
    print("拒绝：超出单次上限")
elif remaining < 0:
    print("拒绝：超出日预算")
else:                                #else:前面三个条件都不满足：模型在白名单,金额<=50,---->允许调用
    print(f"允许，今日还剩{remaining}元")






