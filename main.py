import src.ExeclUtils as ExeclUtil


def _log():
    print('''
           _                      _______                      _
  _dMMMb._              .adOOOOOOOOOba.              _,dMMMb_
 dP'  ~YMMb            dOOOOOOOOOOOOOOOb            aMMP~  `Yb
 V      ~"Mb          dOOOOOOOOOOOOOOOOOb          dM"~      V
          `Mb.       dOOOOOOOOOOOOOOOOOOOb       ,dM'
           `YMb._   |OOOOOOOOOOOOOOOOOOOOO|   _,dMP'
      __     `YMMM| OP'~"YOOOOOOOOOOOP"~`YO |MMMP'     __
    ,dMMMb.     ~~' OO     `YOOOOOP'     OO `~~     ,dMMMb.
 _,dP~  `YMba_      OOb      `OOO'      dOO      _aMMP'  ~Yb._

             `YMMMM\`OOOo     OOO     oOOO'/MMMMP'
     ,aa.     `~YMMb `OOOb._,dOOOb._,dOOO'dMMP~'       ,aa.
   ,dMYYMba._         `OOOOOOOOOOOOOOOOO'          _,adMYYMb.
  ,MP'   `YMMba._      OOOOOOOOOOOOOOOOO       _,adMMP'   `YM.
  MP'        ~YMMMba._ YOOOOPVVVVVYOOOOP  _,adMMMMP~       `YM
  YMb           ~YMMMM\`OOOOI`````IOOOOO'/MMMMP~           dMP
   `Mb.           `YMMMb`OOOI,,,,,IOOOO'dMMMP'           ,dM'
     `'                  `OObNNNNNdOO'                   `'
                           `~OOOOO~'   =颤抖吧人类们！！= ''')


def auth():
    password = '12345667'
    i = 1
    au = True
    print("注意：密码输错3次将自动退出程序！")
    while au:
        if i == 3:
            au = False
        print('请输入密码' + i.__str__())
        pwd = input()
        if pwd == password:
            au = False
            return 'yes'
        i = i + 1
    return 'no'


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    _log()
    au = auth()
    if au == 'yes':
        while True:
            ExeclUtil.info()
            print('输入任意值继续...(输入exit将结束程序)')
            _exit = input()
            if _exit == 'exit':
                break

