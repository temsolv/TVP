__author__ = "temso"

import seaborn as sb
import matplotlib.pyplot as plt


def main():
    # Upload a ready-made dataset of people who survived on the titanic
    titanic_dataset = sb.load_dataset("titanic")

    # Build histogram from dataset
    sb.barplot(
        x="sex", # x - name of x axis
        y="survived", # y - name of y axis
        hue="embark_town", # hue - groups relevant data and tells how color columns
        ci=None, # ci - confidence interval (vertical stripe on top of the rectangle)
        data=titanic_dataset # data - DataFrame, array, or list of arrays
        )
    
    plt.show()

main()