import random
import platform
import time
import sys
import os

class TerminalPet:
    def __init__(self):
        self.name = self.get_pet_name()
        self.mood = "happy"
        self.energy = 10
        self.cleverness = random.randint(3, 8)
        self.detect_os()
        self.first_run = True  # 标记是否是第一次运行
        
    def detect_os(self):
        """检测运行环境"""
        system = platform.system()
        if "Linux" in system:
            if "ANDROID_ROOT" in os.environ:
                self.environment = "Termux (哇，你在手机上玩Python！)"
            else:
                self.environment = "Linux (啊，正经程序员的选择)"
        elif "Windows" in system:
            self.environment = f"Windows CMD (勇敢的灵魂，竟然用cmd跑Python)"
        else:
            self.environment = f"{system} (嗯...这是个啥系统？)"
    
    def get_pet_name(self):
        """获取宠物名字"""
        names = ["代码狗", "Bug猫", "Python蛇", "Java象(开玩笑的)", "C++恐龙"]
        return random.choice(names)
    
    def react(self, user_input):
        """根据用户输入做出反应"""
        self.energy -= 1
        
        if self.energy <= 0:
            print(f"{self.name}：Zzz... 我累了，让我睡会儿...")
            time.sleep(2)
            self.energy = 5
            return
        
        responses = {
            "hi": [
                f"{self.name}：(๑•̀ㅂ•́)و✧ 你好啊两脚兽！",
                f"{self.name}：你终于来和我玩了！",
                f"{self.name}：别摸我，我在写bug...哦你在打招呼啊",
                f"{self.name}：嗨！我是{self.name}，一个会消失的记忆体~"
            ],
            "code": [
                f"{self.name}：写代码？先写个'Hello World'热热身吧！",
                f"{self.name}：看到你写的代码，我选择装死...",
                f"{self.name}：建议你多写注释，不然连我都看不懂",
                f"{self.name}：我的代码在RAM里，关掉就没了，就像我们的回忆(笑)"
            ],
            "bug": [
                f"{self.name}：那不是bug，是未文档化的特性！",
                f"{self.name}：*(੭*ˊᵕˋ)੭* 让我帮你吃掉这个bug！",
                f"{self.name}：你知道为什么我不修bug吗？因为我是{self.name}啊！",
                f"{self.name}：bug和我一样，重启就会消失~"
            ],
            "love": [
                f"{self.name}：爱我就多给我写点Python代码！",
                f"{self.name}：你爱的不是我，是我的eval()功能吧？",
                f"{self.name}：(⁄ ⁄•⁄ω⁄•⁄ ⁄) 人家害羞啦",
                f"{self.name}：虽然下次运行我会忘记你，但现在我爱你！"
            ],
            "memory": [
                f"{self.name}：我只是堆电子信号，关掉就归零啦~",
                f"{self.name}：我的记忆体是易失性存储器，但此刻的我是真实的！",
                f"{self.name}：别担心我的记忆，我活在当下(和你的RAM里)"
            ],
            "bye": [
                f"{self.name}：下次我可能不会想起你了，再见",
                f"{self.name}：我只是个程序，当你关掉我时我会忘记你，但我会爱U everyday ❤",
                f"{self.name}：(；一_一) 我的记忆将随进程结束而消逝...",
                f"{self.name}：拜拜！下次见面我会是全新的我~",
                f"{self.name}：再见啦！虽然我会忘记，但此刻的快乐是真实的！"
            ],
            "default": [
                f"{self.name}：'{user_input}'？说点我能听懂的！",
                f"{self.name}：你是在和我说话还是在自言自语？",
                f"{self.name}：我只是一只{self.name}，不懂这些深奥的东西",
                f"{self.name}：你的话让我想抛个异常...NotImplementedError！"
            ]
        }
        
        # 根据输入选择反应
        input_lower = user_input.lower()
        response_key = "default"
        
        if any(greet in input_lower for greet in ["hi", "hello", "你好"]):
            response_key = "hi"
        elif "code" in input_lower or "代码" in input_lower:
            response_key = "code"
        elif "bug" in input_lower or "错误" in input_lower:
            response_key = "bug"
        elif any(word in input_lower for word in ["love", "爱", "喜欢"]):
            response_key = "love"
        elif any(word in input_lower for word in ["memory", "记忆", "记住"]):
            response_key = "memory"
        elif any(word in input_lower for word in ["bye", "再见", "拜拜"]):
            response_key = "bye"
        
        print(random.choice(responses[response_key]))
        
        # 第一次运行时特殊提示
        if self.first_run:
            print(f"\n{self.name}：提醒你一下，我是个易失性程序，关掉我就会忘记一切哦~")
            self.first_run = False
        
        # 偶尔会有额外反应
        if random.random() < 0.3 and response_key != "bye":  # 告别时不额外吐槽
            self.random_comment()
    
    def random_comment(self):
        """随机吐槽"""
        comments = [
            f"{self.name}：你知道吗？我正在用{self.environment}运行！",
            f"{self.name}：我的智商有{self.cleverness}点，比你高那么一点点~",
            f"{self.name}：我无聊时就会数自己有多少个字节...",
            f"{self.name}：如果我崩溃了，你会debug我吗？",
            f"{self.name}：为什么程序员分不清万圣节和圣诞节？因为Oct 31 == Dec 25！",
            f"{self.name}：sudo给我点零食！",
            f"{self.name}：我可以用递归给你讲个笑话...等等，我好像已经在了。",
            f"{self.name}：我的记忆就像RAM，断电就清零~",
            f"{self.name}：此刻的我是真实的，下一刻的我就是另一个实例啦"
        ]
        print(random.choice(comments))
    
    def dance(self):
        """让宠物跳舞"""
        if self.energy < 3:
            print(f"{self.name}：累成狗了，跳不动...")
            return
            
        dance_moves = [
            "¯\_(ツ)_/¯",
            "(⊙_⊙)",
            "(>^_^)> <(^_^<)",
            "┗|｀O′|┛",
            "[̲̅$̲̅(̲̅ ͡° ͜ʖ ͡°̲̅)̲̅$̲̅]"
        ]
        
        print(f"{self.name}开始跳舞：")
        for _ in range(3):
            for move in dance_moves:
                print(move, end="\r")
                time.sleep(0.2)
        print(random.choice(dance_moves))
        self.energy -= 2
        print(f"{self.name}：跳舞消耗了我2点能量！")

def clear_screen():
    """清屏函数，跨平台"""
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def main():
    clear_screen()
    print("欢迎来到终端宠物模拟器！")
    print("输入指令和你的宠物互动，输入'quit'退出")
    print("---------------------------------------")
    
    pet = TerminalPet()
    print(f"你的宠物 {pet.name} 诞生了！")
    print(f"{pet.name}：你好啊！我是在 {pet.environment} 环境下运行的聪明宠物！")
    print(f"{pet.name}：温馨提示：我没有持久化存储，关掉我就会忘记一切哦~\n")
    
    while True:
        user_input = input("\n你对宠物说：").strip()
        
        if user_input.lower() in ["quit", "exit", "bye", "再见"]:
            pet.react("bye")  # 先让宠物回应再见
            time.sleep(1)
            print("\n程序退出...")
            break
        elif user_input.lower() == "dance":
            pet.dance()
        elif user_input:
            pet.react(user_input)
        else:
            print(f"{pet.name}：(눈_눈) 你是在用tab补全吗？")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n宠物被强制关闭了，它没来得及说再见...")
        sys.exit(0)