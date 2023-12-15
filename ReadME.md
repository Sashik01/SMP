Statistical Analysis Toolkit
Overview
Welcome to the Statistical Analysis Toolkit! This Python library provides two key statistical tests: Analysis of Variance (ANOVA) and the Kruskal-Wallis Test. These tests are valuable tools for analyzing differences among group means and group medians, respectively.

Features
ANOVA (Analysis of Variance)
The ANOVA class allows you to perform an analysis of variance on a set of groups, testing whether there are any statistically significant differences between the means of the groups. The class includes methods to calculate the F-statistic, p-value, and provides a theoretical interpretation of the results.

Usage Example:

python
Copy code
# Instantiate ANOVA with data and significance level
anova_test = ANOVA(data_array, significance_level)

# Perform ANOVA
anova_test.result()
Kruskal-Wallis Test
The HTest class implements the Kruskal-Wallis Test, a non-parametric alternative to ANOVA suitable for ordinal and interval data. This test assesses whether there are statistically significant differences between the medians of different groups.

Usage Example:

python
Copy code
# Instantiate HTest with data and significance level
h_test = HTest(data_array, significance_level)

# Perform Kruskal-Wallis Test
h_test.result()
Getting Started
Install the required dependencies:

bash
Copy code
pip install numpy scipy
Clone this repository:

bash
Copy code
git clone https://github.com/your_username/statistical-analysis-toolkit.git
Import the classes into your Python script:

python
Copy code
from statistical_analysis_toolkit import ANOVA, HTest
Create an instance of the desired class and perform the statistical test.

Example
python
Copy code
import numpy as np
from statistical_analysis_toolkit import ANOVA, HTest

# Example data for ANOVA
data_array_anova = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
significance_level_anova = 0.05

# Example data for Kruskal-Wallis Test
data_array_h_test = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
significance_level_h_test = 0.05

# Perform ANOVA
anova_test = ANOVA(data_array_anova, significance_level_anova)
anova_test.result()

# Perform Kruskal-Wallis Test
h_test = HTest(data_array_h_test, significance_level_h_test)
h_test.result()
Contribution
Feel free to contribute by forking the repository, making changes, and submitting pull requests. If you encounter any issues or have suggestions for improvement, please create an issue on the GitHub repository.

License
This project is licensed under the MIT License - see the LICENSE file for details.
