import toy_project1127.root_config as root_config
from member import member_service
from order import order_service
from memo import memo_service

def main():
    run = True

    while run:

        menuNum = int(input('1.MEMBER  2.ORDER  3.MEMO 99.SYSTEM-OUT '))

        if menuNum == root_config.MEMBER_SERVICE:
            member_service.MemberService().run()  
            
        elif menuNum == root_config._SERVICE:
            bank_service.BankService().run()
            
        elif menuNum == root_config.MEMO_SERVICE:
            memo_service.MemoService().run()

        elif menuNum == root_config.SYSTEM_OUT:
            run = False 


if __name__ == "__main__":
    main()