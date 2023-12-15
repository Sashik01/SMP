import numpy as np
import scipy

class ANOVA:
    def __init__(self, lists: np.ndarray, sig_lev: float):
        #конструктор
        self.array = lists # array
        self.F_statistic = 0 # F-statistic
        self.p_value = 0 #p_value
        self.sig_lev = sig_lev # significant level
           
    def F_stat(self):
        GM = np.sum([np.mean(i) for i in self.array]) / 3 # general average value of samples
        MSB = (np.sum([(len(i) * ((np.mean(i) - GM) ** 2)) for i in self.array])) / (len(self.array) - 1) # середньоквадратичне відхилення міжгрупової дисперсії
        MSW = (np.sum([(np.sum((j - np.mean(i)) ** 2)) for i in self.array for j in i]))/(np.sum([len(i) for i in self.array]) - (len(self.array) - 1)) # середньоквадратичне відхилення внутрішньогрупової дисперсії

        self.F_statistic = MSB/MSW
        return self.F_statistic
        
    def p_values(self):
        deg_qual = len(self.array) - 1 # (k - 1) Ступені свободи для кількості
        deg_quan = (np.sum([len(i) for i in self.array]) - (len(self.array) - 1)) #(N - k) Ступені свободи для якості
        self.p_value = scipy.stats.f.ppf(1 - self.sig_lev, deg_qual, deg_quan) 
        return self.p_value
    
    def Theory(self):
        if (self.sig_lev > self.p_values()):
            print('Ми не можемо відхилити H0. Немає статистично значущих різниць між середніми значеннями в різних групах.')
            print(f'statistic = {self.F_stat()}, pvalue = {self.p_values()}') 
        else:
            print('Відхиляємо гіпотезу H0. Є статистично значущі різниці між середніми значеннями в різних групах.')
            print(f'statistic = {self.F_stat()}, pvalue = {self.p_values()}')

    def result(self):
        if (len(self.array) < 2):
            print('Error. You make a mistake. Try again.')
        else:
            self.Theory()
        