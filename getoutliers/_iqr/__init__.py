import numpy as np



class IQR:
    """
    IQR
    ===

    It's a class for identify outliers in pandas dataframe

    """
    def __init__(self, data: np.ndarray) -> np.ndarray:
        #Convert the data as an numpy array to be able to work with pandas Dataframe
        self.data = np.asanyarray(data)
        

    

    @property
    def iqr(self):
        """
        The IQR is the 75% of the Series of number minus the 25%

        IQR = Q3 - Q1
        
        >>> x = [1, 2, 3, 4, 5]
        2 (Q1) is the 25% and 4 (Q3) is the 75 %

        """
        Q1 = np.percentile(self.data, 25)
        Q3 = np.percentile(self.data, 75)

        return {"Q1":Q1, "Q3":Q3, "result":Q3 - Q1}

        
    
    def there_lb(self, bool_=True):
        """
        there_lb = "there lower bound"

        The lower bound is the method that gonna say to you,
        if in the specific dataset (pandas Series) has lower bound outliers or not.
        
        """
        iqr = self.iqr["result"]

        q1 = self.iqr["Q1"]

        result = (True if (self.data < (q1 - 1.5 * iqr)).any() else False)

        if bool_ == True:
            return result
        elif bool_ == False:
            return q1 - 1.5 * iqr
        else:
            raise "The value has to be a boolean type, it works with 1 or 0"
    
    def there_up(self, bool_=True):
        """
        there_up = "there upper bound"

        The upper bound is the method that gonna say to you,
        if in the specific dataset (pandas Series) has upper bound outliers or not.
        
        """

        iqr = self.iqr["result"]

        q3 = self.iqr["Q3"]

        result = (True if (self.data > (q3 + 1.5 * iqr)).any() else False)

        if bool_ == True:
            return result
        elif bool_ == False:
            return q3 + 1.5 * iqr
        else:
            raise "The value has to be a boolean type, it works with 1 or 0"
        
        
    def theres_outliers(self, value=False):
        """
        there is outliers ? i dunno
        ---------------------------
        that function gonna answer that question to you.

        If the dataset has outliers, it gonna return a dict that contains
        a boolean value (there_lb? or there_up?) that said if it has (outliers) or not and a
        real number (up_iqr ou lb_iqr).

        If the dataset has a upper bound:

        >>> list = [1, 2, 3, 4, 30]
        >>> x = getoutliers.IQR(list)
        >>> x.there_outliers()
        {'there_up?': True, 'up_iqr': np.float64(7.0)}

        If the dataset has a lower bound:
        >>> list = [-10, 2, 3, 4, 5]
        >>> x = getoutliers.IQR(list)
        >>> x.there_outliers()
        {'there_lb?': True, 'lb_iqr': np.float64(-10)}
        
        """

        if value == False:

            #Check if there two outliers lower bound and upper bound
            #there_outliers gonna return a dict cointains the values of
            #lower bound and upper bound
            if self.there_lb() == True and self.there_up() == True:
                return {"there_lb?":True, "lb_iqr":self.there_lb(bool_=False), "there_up?":
                        True, "up_iqr":self.there_up(bool_=False)}

            #Check if there is a lower bound
            elif self.there_lb() == True:
                return {"there_lb?":True, "lb_iqr":self.there_lb(bool_=False)}
            
            #Check if there is a upper bound
            elif self.there_up() == True:
                return {"there_up?":True, "up_iqr":self.there_up(bool_=False)}
            
            
            
            else:
                return self.data
            

        # If the value is True, that gonna return just the value (outliers) of the dataset    
        elif value == True:

            thereup = self.there_up()
            therelb = self.there_lb()

            # If thereup and therelb are True
            if thereup and therelb:
                # I Created a condition to create an array and return True if a element in self.data is higher than
                # upper bound, And True if a element in self.data is lower than lower bound
                condition = (self.data < self.there_lb(bool_=False)) | (self.data > self.there_up(bool_=False))

                #And put this condition into np.where, to return the index of that element
                # I put [0], coz where method created a tuple, and i take the first index 
                outlier_index = np.where(condition)[0]
                # I took those index in outlier_index to localize the datas.
                outlier_values = self.data[condition]
                return {"index": outlier_index, "value": outlier_values}
            
            elif therelb and not thereup:
                result = np.where(self.data < self.there_lb(bool_=False))
                return {"index": result[0], "value": self.data[result[0]]}
            
            elif thereup and not therelb:
                result = np.where(self.data >= self.there_up(bool_=False))
                return {"index": result[0], "value": self.data[result[0]]}
            
            else:
                return None
        

