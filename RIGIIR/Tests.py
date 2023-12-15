from abc import ABC, abstractmethod
import numpy as np
import scipy
from scipy.stats import rankdata
from scipy.stats import chi2

class Test(ABC):
    def __init__(self, data: np.ndarray, sig_lev: float):
        self.sig_lev = sig_lev  # significant level
        self.data = data  # np.ndarray
        self.statistic = 0
        self.p_value = 0

    @abstractmethod
    def calculate_statistic(self):
        pass

    @abstractmethod
    def calculate_p_value(self):
        pass

    @abstractmethod
    def result(self):
        pass

class ANOVA(Test):
    def __init__(self, lists: np.ndarray, sig_lev: float):
        super().__init__(lists, sig_lev)
           
    def calculate_statistic(self):
        GM = np.sum([np.mean(i) for i in self.data]) / 3 # general average value of samples
        MSB = (np.sum([(len(i) * ((np.mean(i) - GM) ** 2)) for i in self.data])) / (len(self.data) - 1) # середньоквадратичне відхилення міжгрупової дисперсії
        MSW = (np.sum([(np.sum((j - np.mean(i)) ** 2)) for i in self.data for j in i]))/(np.sum([len(i) for i in self.data]) - (len(self.data) - 1)) # середньоквадратичне відхилення внутрішньогрупової дисперсії

        self.statistic = MSB/MSW
        return self.statistic
        
    def calculate_p_value(self):
        deg_qual = len(self.data) - 1 # (k - 1) Ступені свободи для кількості
        deg_quan = (np.sum([len(i) for i in self.data]) - (len(self.data) - 1)) #(N - k) Ступені свободи для якості
        self.p_value = scipy.stats.f.ppf(1 - self.sig_lev, deg_qual, deg_quan) 
        return self.p_value
    
    def Theory(self):
        if (self.sig_lev > self.calculate_p_value()):
            print('Ми не можемо відхилити H0. Немає статистично значущих різниць між середніми значеннями в різних групах.')
            print(f'statistic = {self.calculate_statistic()}, pvalue = {self.calculate_p_value()}') 
        else:
            print('Відхиляємо гіпотезу H0. Є статистично значущі різниці між середніми значеннями в різних групах.')
            print(f'statistic = {self.calculate_statistic()}, pvalue = {self.calculate_p_value()}')

    def result(self):
        if (len(self.data) < 2):
            print('Error. You make a mistake. Try again.')
        else:
            self.Theory()

class HTest(Test):
    def __init__(self, lists: np.ndarray, sig_lev: float):
        super().__init__(lists, sig_lev)
        self.reshaped_data = np.array([])  # matrix_average
        self.ranks_grouped = np.array([])
        self.reshaped_groups = self.data.reshape((len(self.data[0]), len(self.data))) # for visualization matrix
        self.datas = np.sort(np.concatenate(self.data)) # np.array(general)
        self.ranks_avg = rankdata(self.datas, method='average') #ranks
        self.reshaped_data = np.array([]) # matrix_average

    def formed_ranks(self):        
        num_col = len(self.data)
        num_rows = int(len(self.ranks_avg) / num_col)
        self.reshaped_data = self.ranks_avg.reshape((num_rows, num_col))   
        self.ranks_grouped = np.sum(self.reshaped_data, axis=0)
        return None

    def calculate_statistic(self):
        N = len(self.data) * len(self.data[0]) 
        k = len(self.data)
        T = np.array(sum([((self.ranks_grouped[i] ** 2) / len(self.reshaped_data)) for i in range(len((self.reshaped_data[0])))])) # R^2 / n
        self.statistic = (12 / N * (N + 1)) * (T - 3 * (N + 1))  # Тут може бути помилка з сумою, перепитати
        return self.statistic

    def calculate_p_value(self):
        k = len(self.data)
        dk = len(self.data) - 1
        H = self.calculate_statistic()
        self.p_value = 1 - chi2.cdf(H, dk)
        return self.p_value
    
    def result(self):
        self.formed_ranks()
        if (self.sig_lev > self.calculate_p_value()):
            print('Є статистично значущі різниці між медіанами хоча б двох груп.')
            print(f'statistic = {self.statistic}, pvalue = {self.p_value}')
        else:
            print('Медіани всіх груп рівні (немає статистично значущих відмінностей).')
            print(f'statistic = {self.statistic}, pvalue = {self.p_value}')     