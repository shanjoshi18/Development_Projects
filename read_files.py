import os
import sys
import pandas as pd

class FileProcessing:

    def __init__(self, folder_path,out_path):
        self.folder_path = folder_path
        self.out_path = out_path

    def list_files(self):
        entries = os.listdir(self.folder_path)
        files = [self.folder_path+'/'+item for item in entries]
        return files

    def read_files(self, files_list):
        final_df = None
        for file in files_list:
            print(file)
            try:
                df = pd.read_csv(file, delimiter='\t')
                if final_df is None:
                    final_df = df.copy()
                else:
                    final_df = pd.concat([final_df, df], ignore_index=True)
            except Exception as e:
                print(e)
        final_df = final_df.drop_duplicates()
        return final_df

    def filter_dataframes(self, dataframe):
        dataframe['Gross Salary'] = dataframe['allowances'] + dataframe['basic_salary']
        df = dataframe.sort_values(by='Gross Salary', ascending=False)
        second_highest_salary = df['Gross Salary'].iloc[1]
        average_salary = df['Gross Salary'].mean()
        print(second_highest_salary)
        print(average_salary)
        list_cols = df.columns
        dict_col = {}
        for item in list_cols:
            if item == 'id':
                dict_col[item] = f'Second Highest Salary = {second_highest_salary}'
            elif item == 'first_name':
                dict_col[item] = f'average salary = {average_salary}'
            else:
                dict_col[item] = ''
        df_footer = pd.DataFrame.from_dict(dict_col, orient='index').T
        final_df = pd.concat([dataframe, df_footer], ignore_index=True)
        return final_df

    def save_file(self, df):
        df.to_csv(self.out_path, index=False)

