import pandas as pd
import numpy as np
from wrapers import time_of_functions,result_printer


@time_of_functions
@result_printer(True)
def read_data(filename_csv):
    fixed_df = pd.read_csv(filename_csv,sep=',', encoding='latin1')
    return fixed_df

@time_of_functions
@result_printer(False)
def count_number_times(df):
    result=(len(set(df['period_id'])))
    return result

@time_of_functions
@result_printer(False)
def count_number_times_2(df):
    result=len(df.groupby(['period_id']).size().reset_index(name='count'))
    return result


@time_of_functions
@result_printer(False)
def average_periods(df,number_of_periods):
    result=len(df)/number_of_periods
    return "Средняя продолжительность промопериода {} недель".format (result)

@time_of_functions
@result_printer(False)
def average_periods_2(df):
    df_count = df.groupby(['period_id']).size().reset_index(name='count')
    result=df_count["count"].mean()
    return "Проверка формулы для медианы.Средняя продолжительность промопериода {} недель".format(result)


@time_of_functions
@result_printer(False)
def median_periods(df):
    column=sorted(list(df['period_id']))
    lengthes = np.array([column.count(i) for i in set(column)])
    result=np.median(lengthes)
    return "Медиана промопериода {} недель".format(result)


@time_of_functions
@result_printer(False)
def median_periods_2(df):
    df_count = df.groupby(['period_id']).size().reset_index(name='count')
    result=df_count["count"].median()
    return "Медиана промопериода {} недель".format(result)

@time_of_functions
@result_printer(False)
def sales_volume(df):
    periods = set(df['period_id'])
    result=[{"period_id":i,"sum_volume":df.loc[df['period_id'] == i,"sales_volume"].sum()} for i in periods]
    #result=[["period_id"],"sum_volume":i["sum"]["sales_volume"].sum()} for i in volume]
    return result

@time_of_functions
@result_printer(False)
def average_periods_store(df):
    stores = set(df['store_id'])
    result=len(df)/len(stores)
    return "Среднее количество промопериодов в магазине - "+str(result)

@time_of_functions
@result_printer(False)
def average_periods_store_1(df):
    stores = set(df['store_id'])
    number_periods = sorted([len(df.loc[df['store_id'] == i, "period_id"]) for i in stores])
    result=np.average(np.array(number_periods))
    return "Проверка формулы для медианы. Среднее количество промопериодов в магазине - {}".format(result)

@time_of_functions
@result_printer(False)
def median_periods_store(df):
    stores = set(df['store_id'])
    number_periods=sorted([len(df.loc[df['store_id'] == i,"period_id"]) for i in stores])
    median_index=int(len(number_periods)/2)
    result=number_periods[median_index]
    return str(result) +" промопериодов"


@time_of_functions
@result_printer(False)
def median_periods_store_2(df):
    #result=df.assign().pivot_table(index='store_id', columns='period_id', aggfunc='size', fill_value=0).reset_index()#.rename_axis(None, 1)
    df_count = df.groupby(['store_id']).size().reset_index(name='count')
    result = df_count["count"].median()
    return "Медиана количества промопериодов в магазинах - " + str(result)

df=read_data('milk_promo_sales.csv')

'''Общее количество промопериодов'''
count_number_times(df)
number_of_periods=count_number_times_2(df)

'''Медиана продолжительности промопериода'''
average_periods(df,number_of_periods)
average_periods_2(df)
median_periods(df)
median_periods_2(df)

'''Объем продаж по каждому промопериоду'''
sales_volume(df)

'''Медиана количества промопериодов на один магазин'''
average_periods_store(df)
average_periods_store_1(df)
median_periods_store(df)
median_periods_store_2(df)

