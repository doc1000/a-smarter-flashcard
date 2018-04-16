import re
import pandas as pd


def read_cards(file_path):
    '''
    INPUT: file_path with string of file holding flash card data

    OUTPUT: dataframe representing values read from file
    '''
    df = pd.read_csv(file_path, sep='\t', names=['question','answer'])
    return df

def clean_dataframe(df):
    df2 = df.copy()

    # Remove html
    df2['question'] = df['question'].map(lambda x: strip_html(x))
    df2['answer']   = df['answer'].map(lambda x: strip_html(str(x)))

    return df2

def strip_html(raw_html):
    '''
    INPUT:   string, potentially with html

    RETURNS: string of the text with html removed
    '''
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, ' ', raw_html)
    return cleantext


''' ######################################################################## '''
if __name__ == '__main__':
    strp_test = '''<br> 'ighted sum  '''
    print(strip_html(strp_test))
