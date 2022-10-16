# Нашей компании нужно сгруппировать клиентов для АБ-тестов. 
# Алгоритм группировки очень простой - взять ID клиента (состоит из 5-7 цифр, например 7412567) и найти сумму всех его цифр. 
# Получившееся число и является номером группы, в которую входит данный клиент.

def make_group(id):
    sum=0
    for i in str(id):
        sum+=int(i)
    return sum

# Функция, которая подсчитывает число покупателей, попадающих в каждую группу, если нумерация ID сквозная и начинается с 0. 
# На вход функция получает целое число n_customers (количество клиентов).

def count_customers(n_customers):
    dict_group={}
    for id in range(n_customers):
        group=make_group(id)
        if dict_group.get(group)==None:
            dict_group[group]=1
        else:
            dict_group[group]+=1
    return dict_group

#Количество в группе необходимо вызвать 
a=count_customers(100000)
print(a)

# Функция, аналогичная первой, если ID начинается с произвольного числа.
# На вход функция получает целые числа: n_customers (количество клиентов) и n_first_id (первый ID в последовательности).

def count_customers_2(n_customers,n_first_id):
    dict_group={}
    start=n_first_id
    end=n_first_id+n_customers
    for id in range(start, end):
        group=make_group(id)
        if dict_group.get(group)==None:
            dict_group[group]=1
        else:
            dict_group[group]+=1
    return dict_group

b=count_customers_2(100000,1000)
print(b)