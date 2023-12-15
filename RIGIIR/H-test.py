import numpy as np
import scipy
from scipy.stats import rankdata
from scipy.stats import chi2

class HTest:
    def __init__(self, lists: np.ndarray, sig_lev: float):
        self.sig_lev = sig_lev # significant level
        self.groups = lists # np.ndarray
        self.reshaped_groups = self.groups.reshape((len(lists[0]), len(lists))) # for visualization matrix
        self.data = np.sort(np.concatenate(self.groups)) # np.array(general)
        self.ranks_avg = rankdata(self.data, method='average') #ranks
        self.reshaped_data = np.array([]) # matrix_average
        self.h_statistic, self.p_value = 0, 0

    def formed_ranks(self):        
        num_col = len(self.groups)
        num_rows = int(len(self.ranks_avg) / num_col)
        self.reshaped_data = self.ranks_avg.reshape((num_rows, num_col))   
        self.ranks_grouped = np.sum(self.reshaped_data, axis=0)
        return None

    def calculate_h_statistic(self):
        N = len(self.groups) * len(self.groups[0]) 
        k = len(self.groups)
        T = np.array(sum([((self.ranks_grouped[i] ** 2) / len(self.reshaped_data)) for i in range(len((self.reshaped_data[0])))])) # R^2 / n
        self.h_statistic = (12 / N * (N + 1)) * (T - 3 * (N + 1))  # Тут може бути помилка з сумою, перепитати
        return self.h_statistic

    def calculate_p_value(self):
        k = len(self.groups)
        dk = len(self.groups) - 1
        H = self.calculate_h_statistic()
        self.p_value = 1 - chi2.cdf(H, dk)
        return self.p_value
    
    def result(self):
        self.formed_ranks()
        if (self.sig_lev > self.calculate_p_value()):
            print('Є статистично значущі різниці між медіанами хоча б двох груп.')
            print(f'statistic = {self.h_statistic}, pvalue = {self.p_value}')
        else:
            print('Медіани всіх груп рівні (немає статистично значущих відмінностей).')
            print(f'statistic = {self.h_statistic}, pvalue = {self.p_value}')