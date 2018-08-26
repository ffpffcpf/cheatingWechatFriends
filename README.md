# Usage:
1. core.start_scheduler中的胡汉三是你希望接收信息的用户（微信备注、微信号、微信名）

2. core.start_scheduler中的早安是你想要说的话

3. core.push_reply的传参是自动回覆的文字

4. 自动回覆的出发条件是已经发送了定时消息，且接收方发送内容是文本或表情  


# Todo List:  
1. 封装消息的实体，用于更好维护信息体  
2. 编写单元测试  
3. 抽象出消息处理的类  