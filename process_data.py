import sys
import pandas as pd
import numpy as np
import sqlite3
from sqlalchemy import create_engine

def load_data(messages_filepath, categories_filepath):
    """
    Function to load and merge data
    
    Arguments:
        messages_filepath: messages.csv filepath
        categories_filepath: categories.csv filepath
    Output:
        df -> message and categories csv files merged into 
        a pandas dataframe
    """
    messages = pd.read_csv(messages_filepath)
    categories = pd.read_csv(categories_filepath)
    df = pd.merge(messages,categories,on='id')
    return df 

def clean_data(df):
    """
    Data cleaning function. Splits category data into separate columns
    and removes duplicate data.
    
    Arguments:
        df -> Pandas dataframe produced by load_data function
    Outputs:
        df -> cleaned dataframe
    """
    categories = df['categories'].str.split(pat=';', expand=True)
    row = df['categories'].str.split(pat=';', expand=True)
    category_colnames = row.iloc[0]
    category_colnames = category_colnames.apply(lambda x:x[:-2])
    categories.columns = category_colnames
    for column in categories:
        # set each value to be the last character of the string
        categories[column] = categories[column].str[-1]
        # convert column from string to numeric
        categories[column] = categories[column].astype(int)
        # drop the original categories column from `df`
    df=df.drop('categories', axis = 1)
    # concatenate the original dataframe with the new `categories` dataframe
    df = pd.concat([df,categories], axis=1)
    # drop duplicates
    df = df.drop_duplicates()
    return df
        

def save_data(df, database_filename):
    engine = create_engine('sqlite:///DisasterResponse.db')
    df.to_sql('disaster_data', engine, index=False, if_exists='replace')  


def main():
    if len(sys.argv) == 4:

        messages_filepath, categories_filepath, database_filepath = sys.argv[1:]

        print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'
              .format(messages_filepath, categories_filepath))
        df = load_data(messages_filepath, categories_filepath)

        print('Cleaning data...')
        df = clean_data(df)
        
        print('Saving data...\n    DATABASE: {}'.format(database_filepath))
        save_data(df, database_filepath)
        
        print('Cleaned data saved to database!')
    
    else:
        print('Please provide the filepaths of the messages and categories '\
              'datasets as the first and second argument respectively, as '\
              'well as the filepath of the database to save the cleaned data '\
              'to as the third argument. \n\nExample: python process_data.py '\
              'disaster_messages.csv disaster_categories.csv '\
              'DisasterResponse.db')


if __name__ == '__main__':
    main()