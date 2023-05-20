class DataModel:
    def __init__(self):
        self._badwine = None
        self._confusion_matrix = None
        self._csv_id = None
        self._f1score = None
        self._goodwine = None
        self._performance = None
        self._precision = None
        self._recall = None
        self._ypred = None
        self._ytest = None

    @property
    def badwine(self):
        return self._badwine

    @badwine.setter
    def badwine(self, value):
        self._badwine = value

    @property
    def confusion_matrix(self):
        return self._confusion_matrix

    @confusion_matrix.setter
    def confusion_matrix(self, value):
        self._confusion_matrix = value

    @property
    def csv_id(self):
        return self._csv_id

    @csv_id.setter
    def csv_id(self, value):
        self._csv_id = value

    @property
    def f1score(self):
        return self._f1score

    @f1score.setter
    def f1score(self, value):
        self._f1score = value

    @property
    def goodwine(self):
        return self._goodwine

    @goodwine.setter
    def goodwine(self, value):
        self._goodwine = value

    @property
    def performance(self):
        return self._performance

    @performance.setter
    def performance(self, value):
        self._performance = value

    @property
    def precision(self):
        return self._precision

    @precision.setter
    def precision(self, value):
        self._precision = value

    @property
    def recall(self):
        return self._recall

    @recall.setter
    def recall(self, value):
        self._recall = value

    @property
    def ypred(self):
        return self._ypred

    @ypred.setter
    def ypred(self, value):
        self._ypred = value

    @property
    def ytest(self):
        return self._ytest

    @ytest.setter
    def ytest(self, value):
        self._ytest = value
