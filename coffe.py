Menu = {
    'americano': {
        'ingredients' :{
            'water' : 250,
            'coffee' : 18,
        },
        'cost' : 1500
    },
    'latte' : {
        'ingredients' : {
            'water' : 200,
            'coffee' : 24,
            'milk' : 150,
        },
        'cost' : 2500
    },
    'cappuccino' : {
        'ingredients' :{
            'water' : 250,
            'coffee' : 24,
            'milk' : 100,
        },
        'cost' : 3000,
    }
}

# 수익
profit = 0

# 자판기에 있는 재료 자원
resources = {
    'water' : 700,
    'milk' : 300,
    'coffee' : 200,
}
class Coffee:
    profit = 0
    def __init__(self,Menu,resources):
        self.Menu = Menu
        self.resources = resources

    def report(self):
        print('현재 제고입니다.')
        print('물 :'+str(self.resources['water'])+'ml')
        print('우유 :'+str(self.resources['milk'])+'ml')
        print('커피 :'+str(self.resources['coffee'])+'g')
        print('돈 : '+str(Coffee.profit)+'원')
    
    
        


def coffee_prompt():
    while True:
      try:
        coffe_name = input('어떤 커피를 원하세요? (아메리카노/라떼/카푸치노)')
        if coffe_name in Menu.keys():
           enough(coffe_name)
           return False
        elif coffe_name == 'report':
          rp = Coffee(Menu,resources)
          print(rp.report())# 커피 제고, 돈 출력
        elif coffe_name == 'off':
            print('안녕히 가세요.')
            return False
        else:
          raise ValueError
      except ValueError:
        print('올바르지 않은 입력입니다. 다시 입력해 주세요')
        

def enough(coffee_name):
    coffee_name_stuff = Menu[coffee_name]['ingredients']
    user_w= coffee_name_stuff['water']
    user_m= coffee_name_stuff['milk']
    user_c= coffee_name_stuff['coffee']
    re = Coffee(Menu,resources)
    resor_w = re.resources['water']
    resor_m = re.resources['milk']
    resor_c = re.resources['coffee']
    if user_w > resor_w or user_m > resor_m or user_c > resor_c:
      print('재료가 부족합니다')
    else:
      put_ur_money(coffee_name)
      

def put_ur_money(coffee_name):
    ur_coffee_m = Menu[coffee_name]['cost']
    print(f'{ur_coffee_m:,} 입니다. 돈을 넣어주세요')
    # man = 
    # ochun = 
    # chun = 
    # obec = 
    # bec = 
    # oship = 
    # ship = 
    
    
  
coffee_prompt()