import pandas as pd

class Helper:
    def __init__(self):
        return

    def shift_column_to_i(self, df, col_name, i):
        cols = df.columns.tolist()
        cols.remove(col_name)
        cols.insert(i, col_name)
        return df[cols]

    def move_column_after(self, df, col_name, after_col):
        """
        Moves a column in a Pandas DataFrame after another column with a given name.

        Parameters:
            df (pandas.DataFrame): The DataFrame containing the column to move.
            col_name (str): The name of the column to move.
            after_col (str): The name of the column after which to move the column.

        Returns:
            pandas.DataFrame: The modified DataFrame with the column moved to the new position.
        """
        # Get the index of the after_col
        after_col_idx = df.columns.get_loc(after_col)
        # Remove the col_name from the DataFrame
        col = df.pop(col_name)
        # Insert the col_name after the after_col
        df.insert(after_col_idx + 1, col_name, col)
        return df


    def remove_whitespace_from_column_names(self, df):
        df.columns = df.columns.str.strip()
        df.columns = df.columns.str.lstrip()
        return df

    def strip_string_columns(self, df):
        """
        Strips leading and trailing white spaces from all string columns in a pandas DataFrame.
        """
        return df.applymap(lambda x: x.strip() if isinstance(x, str) else x)