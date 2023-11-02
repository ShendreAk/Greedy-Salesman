import pickle 
import datetime
import pandas as pd



class FBPredictions:
    def __init__(self, model_name: str) -> None:
        """
        model name to be loaded for prediction
        """
        with open(
            f"/Users/akshayshendre/Desktop/sales/models/{model_name}.pkl",
            "rb",
        ) as fin:
            try:
                self.model = pickle.load(fin)
            except OSError:
                print("wrong path/ model not available")
                exit(-1)

    def predict(self, prev_date: str):
        """
        Predicts gold prices for next date
        date_format = yyyy-mm-dd
        """
        input_dt = pd.to_datetime(prev_date)

    # first replace day number with 1
        input_dt = input_dt.replace(day=1)

    # add 32 days to the input datetime
        input_dt = input_dt + datetime.timedelta(days=32)

    # replace day number with 1
        self.next_date = input_dt.replace(day=1)
        self.next_date = self.next_date.strftime("%Y-%m-%d")

        next_date_series = pd.DataFrame(
            {"ds": pd.date_range(start=self.next_date, end=self.next_date)}
        )

        pred = self.model.predict(next_date_series)

        return pred

    def get_next_date(self):
        self.next_date = pd.to_datetime(self.next_date)
        return self.next_date.strftime("%Y-%m-%d")

    def plot(self, pred):
        self.model.plot(pred)

class SARIMAPredictions:
    def __init__(self, model_name: str) -> None:
        """
        model name to be loaded for prediction
        """
        with open(
            f"/Users/akshayshendre/Desktop/sales/models/{model_name}.pkl",
            "rb",
        ) as fin:
            try:
                self.model = pickle.load(fin)
            except OSError:
                print("wrong path/ model not available")
                exit(-1)

    def predict(self, prev_date: str):
        """
        Predicts gold prices for next date
        date_format = yyyy-mm-dd
        """
        input_dt = pd.to_datetime(prev_date)

    # first replace day number with 1
        input_dt = input_dt.replace(day=1)

    # add 32 days to the input datetime
        input_dt = input_dt + datetime.timedelta(days=32)

    # replace day number with 1
        self.next_date = input_dt.replace(day=1)
        

        # next_date_series = pd.DataFrame({"ds": pd.date_range(start=self.next_date, end=self.next_date)})
        res = self.model.fit()
        pred = res.predict(self.next_date)

        return pred

    def get_next_date(self):
        
        return self.next_date.strftime("%Y-%m-%d")

    def plot(self, pred):
        self.model.plot(pred)


# testing
if __name__ == "__main__":
    pr = FBPredictions("fbprophet")
    pred = pr.predict("2022-10-12")
    print(pred)