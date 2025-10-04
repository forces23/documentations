from datetime import datetime


def show_date() -> None:
    print('the Date is: ', datetime.now().date())


def show_time() -> None:
    print('the time is: ', datetime.now().time())
    
def greet(name: str) -> None:
    print(f'hello, {name}!')
    
def add(a:float, b:float) -> float:
    return a + b


greet('Bobby')
greet('Caroline')
show_date()
show_time()


result = add(5.5, 4.5)
print('the result is: ', result)