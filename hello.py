import decora
from decora import questions
import time

q0 = questions[0] #vibe
q1 =  questions[1] #color
q2 = questions[2] #type of furniture (stylistic)
q3 = questions[3] #furntiure article identify


url_inp = 'C:/Users/ishan/Downloads/pizza.jpg'


def print_pretty_all(url_inp):
    acc =[]
    for i in range(len(questions)):
        acc.append(f'{questions[i]} ={decora.query(url=url_inp,question= questions[i],k=5)}')
    for elem in acc:
        print(elem)
    # vibe = decora.query(url=url_inp,question= q0,k=5)
    # color = decora.query(url=url_inp,question= q1,k=3)
    # style =decora.query(url=url_inp,question= q2,k=3)
    # article =decora.query(url=url_inp,question= q3,k=1)

print_pretty_all(url_inp)


# time.sleep(5)
# print()
# time.sleep(5)

# print()
# time.sleep(5)
# print()



