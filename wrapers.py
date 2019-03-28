import time

with open("z_enter_exit_results_log.txt", "w")as file1:
    pass
with open("z_time_log.txt", "w")as file2:
    pass


# декоратор, записывающий в лог время выполнения произвольной функции
# если функция выполняется несколько раз подряд,
# она записывается в лог 1 раз,
# в лог записывается суммарное время выполнения функций.
def time_of_functions(func_):
    def wraper(*args,**kwargs):
        time1=time.time()
        result_=func_(*args,**kwargs)
        time2=time.time()-time1
        with open("z_time_log.txt", "a+")as file1:
            file1.write("Функция {0} обработана за {1} секунд\n\n".format(func_.__name__,time2))
        return result_
    return wraper


#декоратор, записывающий в лог входы и выходы произвольной функции
def result_printer(need_print):
    def inner_(func_):
        def wraper(*args,**kwargs):
            result_=func_(*args,**kwargs)
            if need_print:
                args_print=[*args]
            else:
                args_print=" Аргументы не показаны "
            try:
                if len(result_>30):
                    result_print=result_[:30]#[i[:30] for i in result_]
                    with open("z_enter_exit_results_log.txt", "a+")as file2:
                        file2.write("Функция: {0}\nс аргументами: {1}\nвернула результат :\n{2}\n\nВсего {3} строк...\n\n".format(func_.__name__,args_print,result_print,len(result_)))
                else:
                    with open("z_enter_exit_results_log.txt", "a+")as file2:
                        file2.write("Функция: {0}\nс аргументами: {1}\nвернула результат :\n{2}\n\n".format(func_.__name__, args_print, result_))
            except:
                with open("z_enter_exit_results_log.txt", "a+")as file2:
                    file2.write("Функция: {0}\nс аргументами: {1}\nвернула результат :\n{2}\n\n".format(func_.__name__,args_print ,result_))

            return result_
        wraper.__name__ = func_.__name__
        return wraper
    return inner_